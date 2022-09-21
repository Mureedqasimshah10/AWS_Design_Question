import aws_cdk as core
import aws_cdk.assertions as assertions

from sprint5_day6.sprint5_day6_stack import Sprint5Day6Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint5_day6/sprint5_day6_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sprint5Day6Stack(app, "sprint5-day6")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
