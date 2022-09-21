from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    Duration,
    Stack,
    aws_lambda as lambda_,
    RemovalPolicy,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_cloudwatch as cloudwatch_,
    aws_iam as iam_,
    aws_sns as sns_,
    aws_cloudwatch_actions as cw_actions_,
    aws_sns_subscriptions as subscriptions_,
    aws_dynamodb as dynamodb_,
    aws_codedeploy as codedeploy_,
    aws_apigateway as apigateway_,
)
from constructs import Construct

class Sprint5Day2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = self.create_lambda_role()
        api_lambda = self.create_lambda("apiLambda", "apiLambda.lambda_handler", "./resources", lambda_role)

        # Add table to environment variables of lambda functions
        APITable = self.API_create_table()
        apitable = APITable.table_name
        api_lambda.add_environment(key="APITable", value=apitable)

        # Giving the API GATEWAY Permission to invoke my api_lambda function
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/Function.html#aws_cdk.aws_lambda.Function.grant_invoke
        api_lambda.grant_invoke(iam_.ServicePrincipal("apigateway.amazonaws.com"))

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/README.html
        # Creating first api
        api_1 = apigateway_.LambdaRestApi(self, "mureed_api_1",
                handler=api_lambda,
                proxy=False,
                )

        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/README.html
        # Creating second api
        api_2 = apigateway_.LambdaRestApi(self, "mureed_api_2",
                handler=api_lambda,
                proxy=False,
                )

        # Define the API CRUD model using addMethod function
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/Resource.html
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway/IResource.html#aws_cdk.aws_apigateway.IResource.add_method
        items = api_1.root.add_resource("root") 
        items.add_method("GET")            # GET Read /items
        items.add_method("POST")           # POST Create /items

        items = api_2.root.add_resource("root") 
        items.add_method("GET")            # GET Read /items
        items.add_method("POST")           # POST Create /items

    # Creating the lambda function
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/Function.html
    def create_lambda(self, id_, handler, path, my_role):
        return lambda_.Function(self, id_,
        runtime=lambda_.Runtime.PYTHON_3_8,
        handler=handler,
        code=lambda_.Code.from_asset(path), 
        role= my_role,
        timeout=Duration.seconds(30)
    )

    # Creating iam role for my lambda function
    def create_lambda_role(self):
        lambda_role = iam_.Role(self, "lambda_role",
        assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
        managed_policies=[ 
                            iam_.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'),
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess')
                        ])
        return lambda_role  
    # Creating an API Table
    def API_create_table(self):
        return dynamodb_.Table(self, "QasimAPILambdaInfoTable",
        removal_policy=RemovalPolicy.DESTROY,
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_dynamodb/Attribute.html#aws_cdk.aws_dynamodb.Attribute
        partition_key = dynamodb_.Attribute(name="attr1", type=dynamodb_.AttributeType.STRING),
        sort_key = dynamodb_.Attribute(name="requestTime", type=dynamodb_.AttributeType.STRING)
    )