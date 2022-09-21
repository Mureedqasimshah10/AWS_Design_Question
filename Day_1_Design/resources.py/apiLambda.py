from argparse import Namespace
import resource
from tracemalloc import Statistic
from urllib import response
import boto3
import json
import os
NAMESPACE = "sprint5_day1"
METRICNAME = "qasim_metric"

def lambda_handler(event, context):
    createAlarmclient = boto3.client("cloudwatch")
    snsARN = os.environ["snsARN"]
    body = event["body"]
    value = int(body[8:11])
    dimensions = [{'Name': 'arg1', 'Value':str(value)}]

    matric_data = createAlarmclient.put_metric_data(Namespace = NAMESPACE,
                                    MetricData = [

        {
                # Defining the first matric name, dimension and value
                'MetricName': METRICNAME,
                'Dimensions': dimensions,
                'Value': value,  


            }, 
    ]
    ) 

    createAlarmclient.put_metric_alarm(

        AlarmName = "Qasim_alarm",
        ComparisonOperator = "GreaterThanThreshold",
        EvaluationPeriods = 1,
        MetricName = METRICNAME,
        Namespace = NAMESPACE,
        Period = 60,
        Statistic = "Average",
        Threshold = 10,
        Dimensions = dimensions,
        ActionsEnabled = True,
        AlarmActions = [snsARN]

    )
    if event["httpMethod"] == 'PUT':
        response = {
            "statusCode" : 200,
            "body" : event["body"],
            
        }

        return response
    