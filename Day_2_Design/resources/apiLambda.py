from argparse import Namespace
import resource
from tracemalloc import Statistic
from urllib import request, response
import boto3
import json
import os
from datetime import datetime

# Get the resources
dynamodb = boto3.resource("dynamodb")

# Setting the enviornment variable
tableName = os.environ["APITable"]
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    method = event['httpMethod']
    requestTime = event['requestContext']['requestTime']
    now = datetime.now()
    is_date = now.isoformat()
    body = event['body']
    print(event)
    # Defining the POST Method
    if method == 'POST':
        # get the value
        jso = json.loads(body)
        value = int(jso[0]['event1']['attr1'])

        key = {
            "attr1": str(value),
            "requestTime": is_date
        }

        response = table.put_item(
            Item = key,
        )

        if response:
            return json_response({"message": "successsfully entered the value"})
        else:
            return json_response({"message": "Response is invalid"})
        # Defining the GET method
    elif method == "GET":
        response = table.scan(Limit=10)['Items']

        if response:
            return json_response(response)
        else:
            return json_response({"message": "table is empty"})

def json_response(data):
    return {
        "statusCode": 200,
        "body": json.dumps(data),
        "headers": {'Content-Type': 'application/json'}
    }