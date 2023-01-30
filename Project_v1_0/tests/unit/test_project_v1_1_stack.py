import aws_cdk as core
import aws_cdk.assertions as assertions
from project_v1_1.project_v1_1_stack import ProjectV11Stack


def test_sqs_queue_created():
    app = core.App()
    stack = ProjectV11Stack(app, "project-v1-1")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = ProjectV11Stack(app, "project-v1-1")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
