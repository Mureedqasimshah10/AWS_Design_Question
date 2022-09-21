from typing_extensions import Self
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
class Sprint5Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = self.create_lambda_role()
        api_lambda  = self.create_lambda("apiLambda", "apiLambda.lambda_handler", "./resources.py", lambda_role)
    
        api = apigateway_.LambdaRestApi(self, "mureed_api",
                handler=api_lambda,
                proxy=False,
                )
        Eresponse = api.root.add_resource("Eresponse")
        Eresponse.add_method("PUT")

        topic = sns_.Topic(self, "Alarmnotification")

        topic_arn = topic.topic_arn

        api_lambda.add_environment("snsARN", topic_arn)
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_sns_subscriptions/EmailSubscription.html
        email_address = "qasim.shah.skipq@gmail.com"
        topic.add_subscription(subscriptions_.EmailSubscription(email_address))
        
    

    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/Function.html
    def create_lambda(self, id_, handler, path, my_role):
        return lambda_.Function(self, id_,
        runtime=lambda_.Runtime.PYTHON_3_8,
        handler=handler,
        code=lambda_.Code.from_asset(path), 
        role= my_role,
        timeout=Duration.seconds(30)
    )
        
    def create_lambda_role(self):
        lambda_role = iam_.Role(self, "lambda_role",
        assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
        managed_policies=[ 
                            iam_.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'),
                            iam_.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess')
                        ])
        return lambda_role  
