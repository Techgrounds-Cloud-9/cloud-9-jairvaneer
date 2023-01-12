from aws_cdk import Stack
from constructs import Construct

# Import Nested Stacks

from CDK_Project.vpc import VPC_Stack
# from CDK_Project.nacl import NACL_Stack
# from CDK_Project.sg import SG_Stack
# from CDK_Project.s3 import S3_Stack
# from CDK_Project.ec2 import Admin_Stack
# from CDK_Project.asg import ASG_Stack
# from CDK_Project.alb import ALB_Stack
# from CDK_Project.backup import Backup_Stack

# Root Stack

class CDKStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc=VPC_Stack(self, "VPC_Stack")
        # self.nacl=NACL_Stack(self,"Network_ACL_Stack")
        # self.sg=SG_Stack(self, "Security_Groups_Stack")
        # self.s3bucket=S3_Stack(self, "S3_Bucket_Stack")
        # self.admin_server=Admin_Stack(self, "Admin_Server_Stack")
        # self.asg=ASG_Stack(self, "Auto_Scaling_Group_Stack")
        # self.alb=ALB_Stack(self, "Application_Load_Balancer_Stack")
        # self.backup=Backup_Stack(self, "Backup_Stack")