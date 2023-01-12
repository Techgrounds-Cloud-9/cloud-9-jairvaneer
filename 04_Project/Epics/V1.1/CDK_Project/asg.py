import aws_cdk as cdk
from aws_cdk import (
    Duration,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    aws_iam as iam,
    aws_s3 as s3
)

from constructs import Construct


class ASG_Stack(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, VPC_Webserver=ec2.Vpc, ASG_sg=ec2.SecurityGroup, scriptbucket=s3, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # Allow EC2 instance to get files from the bucket

        # scriptbucket.grant_read(AS_Group.role)

        # Key Pair Webserver

        self.Web_Keypair=ec2.CfnKeyPair(
            self,
            "Web_Keypair",
            key_name="Web_Keypair",
        )

        ############### Launch Template ###############

        self.ASG_Launch_Temp=ec2.LaunchTemplate(
            self,
            "Launch Template",
            launch_template_name="webserver_template",
            instance_type= ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            role=iam.Role(
                self, 'S3_Access_role',
                assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
                managed_policies=[
                    iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
            ),
            user_data=ec2.UserData.for_linux(),
            security_group=ASG_sg,
            key_name="Web_Keypair",
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8, 
                        encrypted=True,
                        delete_on_termination=True
                    )
                )
            ]
        )

        ############### Auto-Scaling Group ###############

        # Create auto-scaling group which will serve as webserver

        AS_Group= autoscaling.AutoScalingGroup(
            self, 
            "Auto_Scaling_Group",
            vpc=VPC_Webserver,
            auto_scaling_group_name="Auto_Scaling_Group",
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            # instance_type=ec2.InstanceType("t2.micro"),
            # machine_image=ec2.AmazonLinuxImage(),
            key_name="Web_Keypair",
            launch_template=self.ASG_Launch_Temp,
            min_capacity= 1,
            max_capacity= 3,
            health_check=autoscaling.HealthCheck.elb(
            grace=Duration.minutes(30)
            ),
            # block_devices=[
            #     ec2.BlockDevice(
            #         device_name="/dev/xvda",
            #         volume=ec2.BlockDeviceVolume.ebs(
            #             30, 
            #             encrypted=True,
            #             kms_key=EBS_Admin_Key,
            #             delete_on_termination=True
            #         )
            #     )
            # ]
        )

        # Scaling Policy
        AS_Group.scale_on_cpu_utilization(
            "CPU_Auto_Scaling",
            target_utilization_percent=80
        )

        ############### Script Launch ##############

        script_path=AS_Group.user_data.add_s3_download_command(
            bucket=scriptbucket,
            bucket_key="userdata.sh"
        )

        AS_Group.user_data.add_execute_file_command(
            file_path=script_path
        )