from aws_cdk import (
    Duration,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    aws_iam as iam,
)

from constructs import Construct


class ASG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, security_group, s3_bucket, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # Allow EC2 instance to get files from the bucket

        # scriptbucket.grant_read(asg.role)

        # Key Pair Webserver

        self.web_keypair=ec2.CfnKeyPair(
            self,
            "Web_Keypair",
            key_name="Web_Keypair",
        )

        ############### Launch Template ###############

        self.asg_launch_temp=ec2.LaunchTemplate(
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
            security_group=security_group,
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

        asg=autoscaling.AutoScalingGroup(
            self, 
            "Auto_Scaling_Group",
            vpc=vpc,
            auto_scaling_group_name="Auto_Scaling_Group",
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            # key_name="Web_Keypair",
            launch_template=self.asg_launch_temp,
            min_capacity= 1,
            max_capacity= 3,
            health_check=autoscaling.HealthCheck.elb(
            grace=Duration.minutes(30)
            ),
        )

        # Scaling Policy
        asg.scale_on_cpu_utilization(
            "CPU_Auto_Scaling",
            target_utilization_percent=80
        )

        ############### Script Launch ##############

        script_path=asg.user_data.add_s3_download_command(
            bucket=s3_bucket,
            bucket_key="userdata.sh"
        )

        asg.user_data.add_execute_file_command(
            file_path=script_path
        )