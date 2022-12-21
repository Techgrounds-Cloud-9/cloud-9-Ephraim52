#!/usr/bin/env python3
import os

import aws_cdk as cdk

from project_v1_1.vpc_stack import CustomVpcStack


app = cdk.App()
CustomVpcStack(app, "cdkproject")

env=cdk.Environment(account='505659885147', region='eu-west-2')

app.synth()
