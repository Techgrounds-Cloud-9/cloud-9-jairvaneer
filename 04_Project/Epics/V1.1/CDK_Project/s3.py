import aws_cdk as cdk
from aws_cdk import (
    aws_s3 as s3,
    Duration,
    RemovalPolicy,
    aws_s3_deployment as s3deploy,
)

from constructs import Construct


class S3_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        ############### S3 Bucket ###############

        # Create S3 bucket for bootstrap script

        scriptbucket=s3.Bucket(
            self,
            "scriptbucket",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Put userdata.sh from Script folder in S3 bucket

        s3deploy.BucketDeployment(
            self, 
            "BucketDeployment",
            destination_bucket=scriptbucket,
            sources=[s3deploy.Source.asset("./Scripts")]
        )
