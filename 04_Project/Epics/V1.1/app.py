#!/usr/bin/env python3
import os

import aws_cdk as cdk

from CDK_Project.CDKStack import CDKStack


app = cdk.App()
CDKStack(app, "CDKStack",)

app.synth()