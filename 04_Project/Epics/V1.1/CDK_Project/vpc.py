import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    CfnOutput
)

from constructs import Construct

# from CDK_Project.nacl import NACL_Web_Construct, NACL_Admin_Construct
# from CDK_Project.sg import  ALB_SG_Construct, ASG_SG_Construct, Admin_SG_Construct
# from CDK_Project.s3 import S3_Construct
# from CDK_Project.ec2 import Admin_Construct
# from CDK_Project.asg import ASG_Construct
# from CDK_Project.alb import ALB_Construct
# from CDK_Project.backup import Backup_Construct


class VPC_Web_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create Webserver VPC ###############

        self.webserver_vpc=ec2.Vpc(
            self, 
            "WebserverVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            vpc_name="WebserverVPC",
            availability_zones=["eu-central-1a", "eu-central-1b", "eu-central-1c"],
            nat_gateway_subnets=ec2.SubnetSelection(
                subnet_group_name="public_subnet"
            ), 
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public_subnet", 
                    cidr_mask=28, 
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name="private_subnet", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                ),
            ]
        )

class VPC_Admin_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create Adminserver VPC ###############

        self.adminserver_vpc=ec2.Vpc(
            self, 
            "AdminserverVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            vpc_name="AdminserverVPC",
            availability_zones=["eu-central-1a", "eu-central-1b"],
            nat_gateways=0, 
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public_subnet", 
                    cidr_mask=25, 
                    subnet_type=ec2.SubnetType.PUBLIC
                )
            ]
        )