import aws_cdk as core
import aws_cdk.assertions as assertions

from v1.1.v1.1_stack import V11Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in v1.1/v1.1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = V11Stack(app, "v1-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
