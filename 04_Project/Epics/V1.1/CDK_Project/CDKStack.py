from aws_cdk import (
    Stack,
    aws_elasticloadbalancingv2 as elbv2,
)

from constructs import Construct

from CDK_Project.vpc import VPC_Web_Construct, VPC_Admin_Construct
from CDK_Project.vpcp import VPC_Peering_Construct
from CDK_Project.nacl import NACL_Web_Construct, NACL_Admin_Construct
from CDK_Project.sg import  ALB_SG_Construct, ASG_SG_Construct, Admin_SG_Construct
from CDK_Project.s3 import S3_Construct
from CDK_Project.ec2 import Admin_Construct
from CDK_Project.asg import ASG_Construct
from CDK_Project.alb import ALB_Construct
from CDK_Project.alb_asg import ASG_Construct
from CDK_Project.backup import Backup_Construct

class CDKStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### VPC Constructs ###############

        webserver_vpc=VPC_Web_Construct(
            self,
            "VPC_Construct"
        ).webserver_vpc

        adminserver_vpc=VPC_Admin_Construct(
            self,
            "VPC_Admin_Construct"
            ).adminserver_vpc

        ############### VPC Peering Construct ###############

        vpc_peering_connection=VPC_Peering_Construct(
            self,
            "VPC_Peering_Construct",
            vpc1=webserver_vpc,
            vpc2=adminserver_vpc
        )

        ################ Network ACL Constructs ################

        nacl_web=NACL_Web_Construct(
            self,
            "NACL_Webserver_Construct",
            vpc=webserver_vpc,
        )
        nacl_admin=NACL_Admin_Construct(
            self,
            "NACL__Adminserver_Construct",
            vpc=adminserver_vpc
        )

        ############### Security Group Constructs ################

        alb_sg=ALB_SG_Construct(
            self,
            "ALB_SG_Construct",
            vpc=webserver_vpc
        )
        asg_sg=ASG_SG_Construct(
            self, 
            "ASG_SG_Construct",
            vpc=webserver_vpc,
        )
        adminserver_sg=Admin_SG_Construct(
            self,
            "Admin_Server_Security_Group_Construct",
            vpc=adminserver_vpc
        )

        ################ S3 Bucket Construct ################

        scriptbucket=S3_Construct(
            self,
            "Scriptbucket",
        )

        ################ Auto Scaling Group Construct ################

        # asg=ASG_Construct(
        #     self,
        #     "Auto_Scaling_Group_Construct",
        #     vpc=webserver_vpc,
        #     security_group=asg_sg,
        #     s3_bucket=scriptbucket
        # )

        ################ Admin Server Construct ################

        adminserver=Admin_Construct(
            self,
            "Admin_Server_Construct",
            vpc=adminserver_vpc,
            security_group=adminserver_sg,
        )

        ################ Application Load Balancer Construct ################

        # alb=ALB_Construct(
        #     self,
        #     "ALB_Construct",
        #     vpc=webserver_vpc,
        #     asg=asg,
        # )

        ################ Application Load Balancer & Auto Scaling Group Construct ################

        asg=ASG_Construct(
            self,
            "ASG_Construct",
            vpc=webserver_vpc,
            security_group=asg_sg,
            s3_bucket=scriptbucket
        )
        ################ Backup Construct ################        

        # backup_plan=Backup_Construct(
        #     self,
        #     "Backup_Construct",
        #     asg=asg
        # )