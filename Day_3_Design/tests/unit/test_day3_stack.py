import aws_cdk as core
import aws_cdk.assertions as assertions

from day3.day3_stack import Day3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in day3/day3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Day3Stack(app, "day3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
