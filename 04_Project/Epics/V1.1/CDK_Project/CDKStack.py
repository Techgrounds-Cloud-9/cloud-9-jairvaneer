from aws_cdk import Stack
from constructs import Construct

# Import Various Constructs

from CDK_Project.vpc import VPC_Construct
# from CDK_Project.nacl import NACL_Construct
# from CDK_Project.sg import SG_Construct
from CDK_Project.s3 import S3_Construct
from CDK_Project.ec2 import Admin_Construct
from CDK_Project.asg import ASG_Construct
from CDK_Project.alb import ALB_Construct
from CDK_Project.backup import Backup_Construct

# Root Stack

class CDKStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc=VPC_Construct(self, "VPC_Construct")

        # self.sg=SG_Stack(self, "Security_Groups_Stack")
        s3bucket=S3_Construct(self, "S3_Bucket_Construct")
        # self.admin_server=Admin_Stack(self, "Admin_Server_Stack")
        # self.asg=ASG_Stack(self, "Auto_Scaling_Group_Stack")
        # self.alb=ALB_Stack(self, "Application_Load_Balancer_Stack")
        # self.backup=Backup_Construct(self, "Backup_Construct")

        # self.asg = ASG_Stack(
        # self,
        # "asg",
        # vpc=[vpc_webserver],
        # asg_sg=self.sg_app.asgsg,
        # role=roles_app.role,
        # )