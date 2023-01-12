import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
)

from constructs import Construct
# from cdk_ec2_key_pair import KeyPair

class Admin_Stack(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, VPC_Adminserver=ec2.Vpc, Adminserver_sg=ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

                ############### EC2 Instance ###############

        # Key Pair Admin Server

        self.Admin_Keypair=ec2.CfnKeyPair(
            self,
            "Admin_Keypair",
            key_name="Admin_Keypair",
        )

        # Instance2: Admin server

        self.Adminserver=ec2.Instance(
            self, 
            "Adminserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            vpc=VPC_Adminserver,
            availability_zone="eu-central-1b",
            instance_name= "Adminserver_Instance",
            security_group=Adminserver_sg,
            key_name="Admin_Keypair",
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        30, 
                        encrypted=True,
                        # kms_key=EBS_Admin_Key,
                        delete_on_termination=True
                    )
                )
            ]
        )
