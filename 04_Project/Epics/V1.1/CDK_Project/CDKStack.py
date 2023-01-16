from aws_cdk import (
    Stack,
)

from constructs import Construct

from CDK_Project.vpc import VPC_Web_Construct, VPC_Admin_Construct
from CDK_Project.vpcp import VPC_Peering_Construct
from CDK_Project.nacl import NACL_Web_Construct, NACL_Admin_Construct
from CDK_Project.sg import  ALB_SG_Construct, ASG_SG_Construct, Admin_SG_Construct
from CDK_Project.s3 import S3_Construct
from CDK_Project.ec2 import Admin_Construct
from CDK_Project.asg import ASG_Construct
from CDK_Project.lb import LB_Construct
from CDK_Project.backup import Backup_Construct

class CDKStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### VPC Constructs ###############

        vpc_webserver=VPC_Web_Construct(self, "VPC_Construct").vpc_webserver
        vpc_adminserver=VPC_Admin_Construct(self,"VPC_Admin_Construct").vpc_adminserver

        ############### VPC Peering Construct ###############

        vpc_peering_connection=VPC_Peering_Construct(
            self,
            "VPC_Peering_Construct",
            vpc1=vpc_webserver,
            vpc2=vpc_adminserver
        )

        ################ Network ACL Constructs ################

        nacl_web=NACL_Web_Construct(
            self,
            "NACL_Webserver_Construct",
            vpc=vpc_webserver,
        )
        nacl_admin=NACL_Admin_Construct(
            self,
            "NACL__Adminserver_Construct",
            vpc=vpc_adminserver
        )

        ############### Security Group Constructs ################

        alb_sg=ALB_SG_Construct(
            self,
            "ALB_SG_Construct",
            vpc=vpc_webserver
        )
        asg_sg=ASG_SG_Construct(
            self, 
            "ASG_SG_Construct",
            vpc=vpc_webserver,
        )
        adminserver_sg=Admin_SG_Construct(
            self,
            "Admin_Server_Security_Group_Construct",
            vpc=vpc_adminserver
        )

        ################ S3 Bucket Construct ################

        scriptbucket=S3_Construct(
            self,
            "Scriptbucket",
        )

        ################ Auto Scaling Group Construct ################

        asg=ASG_Construct(
            self,
            "Auto_Scaling_Group_Construct",
            vpc=vpc_webserver,
            security_group=asg_sg,
            s3_bucket=scriptbucket
        )

        ################ Admin Server Construct ################

        adminserver=Admin_Construct(
            self,
            "Admin_Server_Construct",
            vpc=vpc_adminserver,
            security_group=adminserver_sg,
        )

        ################ Application Load Balancer Construct ################

        lb=LB_Construct(
            self,
            "LB_Construct",
            vpc=vpc_webserver,
            # security_group=alb_sg,
            asg=asg
        )

        # ################ Backup Construct ################        

        backup_plan=Backup_Construct(
            self,
            "Backup_Construct",
            asg=asg
        )