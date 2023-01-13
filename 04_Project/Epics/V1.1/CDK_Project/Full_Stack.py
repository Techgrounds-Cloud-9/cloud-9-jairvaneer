"""
CDK-Project V1.1

Infrastructure requirements:
1 Region
2 VPC's, each with 2 public subnets

VPC Peering Connection

VPC Webserver:                   
    1 public subnets, 1 private subnets (10.10.10.0/24)
    Using ALB as load balancer and as proxy
    ALB also changes HTTP connections to HTTPS with TLS 1.2 or better
    Certificate Manager is needed for HTTPS certificates
    ALB also takes care of the Health Checks of the instances.
    Auto Scaling Group in private subnet replacing webserver v1.0 -> no public IP, max 3 webservers
    AMI new VM's from snapshot current webserver
    1 Network ACL allowing HTTP/HTTPS from everywhere, SSH from admin server
    1 Application Load Balancer Security Group, as this is internet-facing
    Daily backup with 7 days retention

VPC Adminserver
    2 public subnets (10.20.20.0/24)
    1 Network ACL allowing SSH/RDP from trusted location and SSH to webserver
    1 EC2 Instance (Windows) placed in subnet eu-central-1b
    1 Admin Security Group

S3 bucket for bootstrap Scripts 

Instance roles and policies

Key Pairs

Backup Vault for webserver data retention

"""

# Importing the necessary libraries 


# from  urllib import response
import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2, 
    aws_iam as iam, 
    aws_backup as backup,
    # aws_ssm as ssm,
    aws_s3 as S3,
    aws_s3_deployment as s3deploy,
    aws_kms as kms,
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
    aws_events as events,
    RemovalPolicy,
    Duration,
    # CfnOutput,
    # App,
    Tags,
    Stack
)

from constructs import Construct
# from aws_cdk.aws_events import Schedule
# from aws_cdk.aws_s3_assets import Asset
# from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
# from aws_cdk.aws_autoscaling import AutoScalingGroup

# Import Various Constructs

# from CDK_Project.vpc import VPC_Construct
# from CDK_Project.nacl import NACL_Construct
# from CDK_Project.sg import SG_Construct
# from CDK_Project.s3 import S3_Construct
# from CDK_Project.ec2 import Admin_Server_Construct
# from CDK_Project.asg import ASG_Construct
# from CDK_Project.lb import LB_Construct
# from CDK_Project.backup import Backup_Construct



# Stack

class CDKStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create 2 VPC's ###############

        # VPC 1 - Webserver VPC

        vpc_webserver=ec2.Vpc(
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
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name="private_subnet", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                ),
            ]
        )

        # VPC 2 - Adminserver VPC

        vpc_adminserver=ec2.Vpc(
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

        ############### VPC Peering ###############

        vpc_peering_connection=ec2.CfnVPCPeeringConnection(
            self, 
            "VPC1_VPC2_Peering_Connection",
            peer_vpc_id=vpc_adminserver.vpc_id,
            vpc_id=vpc_webserver.vpc_id,
        )
        

        # VPC Peering connection from VPC1 to VPC2 through Route Table 

        self.web_to_admin_route=ec2.CfnRoute(
            self,
            "Web_to_Admin_Route",
            route_table_id=vpc_webserver.public_subnets[0].route_table.route_table_id,
            destination_cidr_block=vpc_adminserver.vpc_cidr_block,
            vpc_peering_connection_id=vpc_peering_connection.ref,
        )

        # VPC Peering connection from VPC2 to VPC1 through Route Table 

        self.admin_to_Web_Route=ec2.CfnRoute(
            self,
            "Admin_to_Web_Route",
            route_table_id=vpc_adminserver.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=vpc_webserver.vpc_cidr_block,
            vpc_peering_connection_id=vpc_peering_connection.ref,
        )
# self.cfn_VPCPeering_connection =ec2.CfnVPCPeeringConnection(self, "VPC peering connection",
#             peer_vpc_id = AdminVPC.vpc_id,
#             vpc_id = WebVPC.vpc_id,

#             # the properties below are optional
#             peer_region='eu-central-1',
#             )

#         # Update Route Tables for Peering Connection
#         route_table_web_entry = ec2.CfnRoute(
#             self, 'VPC-Web Peer Route100',
#             route_table_id=WebVPC.public_subnets[0].route_table.route_table_id,
#             destination_cidr_block='10.20.20.0/24',
#             vpc_peering_connection_id=self.cfn_VPCPeering_connection.attr_id,
#         )

#         route_table_admin_entry = ec2.CfnRoute(
#             self, 'VPC-admin Peer Route100',
#             route_table_id=WebVPC.public_subnets[1].route_table.route_table_id,
#             destination_cidr_block='10.10.10.0/24',
#             vpc_peering_connection_id=self.cfn_VPCPeering_connection.attr_id,
#         )

        ############## Network ACL's ###############

        # Network ACL Webserver

        nacl_web=ec2.NetworkAcl(
            self, 
            "WebServer_NACL",
            vpc=vpc_webserver,
            network_acl_name="Webserver_NACL",
            subnet_selection=ec2.SubnetSelection(
                availability_zones=["eu-central-1a", "eu_central 1b", "eu-central-1c"],
                )
        )
        nacl_web.add_entry("Allow_All_Ingress_IPv4_HTTP_to_Webserver",
            cidr= ec2.AclCidr.any_ipv4(),
            rule_number= 100,
            traffic= ec2.AclTraffic.tcp_port(80),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        nacl_web.add_entry("Allow_All_Ingress_IPv6_HTTP_to_Webserver",
            cidr= ec2.AclCidr.any_ipv6(),
            rule_number= 110,
            traffic= ec2.AclTraffic.tcp_port(80),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        nacl_web.add_entry("Allow_All_Ingress_IPv4_HTTPS_to_Webserver",
            cidr= ec2.AclCidr.any_ipv4(),
            rule_number= 120,
            traffic= ec2.AclTraffic.tcp_port(443),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        nacl_web.add_entry("Allow_All_Ingress_IPv6_HTTPS_to_Webserver",
            cidr= ec2.AclCidr.any_ipv6(),
            rule_number= 130,
            traffic= ec2.AclTraffic.tcp_port(443),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        nacl_web.add_entry("Allow_Ingress_SSH_from_Adminserver",
            cidr= ec2.AclCidr.ipv4("10.20.20.128/25"),
            rule_number= 140,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )                        
        nacl_web.add_entry("Allow_Ingress_Ephemeral_Ipv6",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=150,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS, 
            rule_action=ec2.Action.ALLOW,
        )       
        nacl_web.add_entry("Allow_Ingress_Ephemeral_IPv6",
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=160,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS, 
            rule_action=ec2.Action.ALLOW,
        )
        nacl_web.add_entry("Allow_All_Egress_Ipv4",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS, 
            rule_action=ec2.Action.ALLOW,
        )
        nacl_web.add_entry("Allow_All_Egress_IPv6",
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=110,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS, 
            rule_action=ec2.Action.ALLOW,
        )

        # # Network ACL Admin Server

        nacl_admin = ec2.NetworkAcl(
            self, 
            "Adminserver_NACL", 
            vpc = vpc_adminserver,
            network_acl_name="Adminserver_NACL",
            subnet_selection=ec2.SubnetSelection(
                availability_zones=["eu-central-1b"],
                )
        )
        nacl_admin.add_entry("Allow_Admin_Ingress_SSH_to_Adminserver_IPv4",
            cidr= ec2.AclCidr.ipv4("178.85.64.168/32"),
            rule_number= 100,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        nacl_admin.add_entry("Allow_Admin_Ingress_RDP_to_Adminserver_IPv4",
            cidr= ec2.AclCidr.ipv4("178.85.64.168/32"),
            rule_number= 110,
            traffic= ec2.AclTraffic.tcp_port(3389),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )  
        nacl_admin.add_entry("Allow_Admin_Ingress_RDP_to_Adminserver_IPv6",
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )
        nacl_admin.add_entry("Allow_Ingress_Ephemeral_IPv4_from_Webserver",
            cidr=ec2.AclCidr.ipv4("10.10.10.0/25"),
            rule_number=130,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS, 
            rule_action=ec2.Action.ALLOW,
        )
        nacl_admin.add_entry("Allow_All_Egress_IPv4",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS, 
            rule_action=ec2.Action.ALLOW,
        )

        ############### Security Groups ###############

        # Security Group Auto Scaling Group

        asg_sg = ec2.SecurityGroup(
            self, 
            "Auto_Scaling_Group_Security_Group",
            vpc= vpc_webserver,
            description= "Security group of the Auto Scaling Group",
            allow_all_outbound=True
        )
        asg_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(), 
            connection= ec2.Port.tcp(80), 
            description= "allow IPv4 HTTP access from the world"
        )
        asg_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(), 
            connection= ec2.Port.tcp(443), 
            description= "allow IPv4 HTTPS acccess from the world"
        )
        asg_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(80), 
            description= "allow IPv6 HTTP acccess from the world"
        )
        asg_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(443), 
            description= "allow IPv6 HTTPS acccess from the world"
        )
        asg_sg.add_ingress_rule(
            peer= ec2.Peer.ipv4("10.20.20.128/25"), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from Admin Server IP adress"
        )

        # Security Group Admin Server

        adminserver_sg = ec2.SecurityGroup(
            self, 
            "Adminserver_Security_Group",
            vpc=vpc_adminserver,
            description= "Security group of the Adminserver",
            allow_all_outbound=True
        )
        adminserver_sg.add_ingress_rule(
            peer= ec2.Peer.ipv4("178.85.64.168/32"), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from admin IPv4 adress"
        )
        adminserver_sg.add_ingress_rule(
            peer= ec2.Peer.ipv4("178.85.64.168/32"), 
            connection= ec2.Port.tcp(3389), 
            description= "allow RDP access from admin IPv4 adress"
        )
        adminserver_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(3389), 
            description= "allow RDP access from admin IPv6 adress"
        )        
        adminserver_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from admin IPv6 adress"
        )

        # Security Group Application Load Balancer

        alb_sg = ec2.SecurityGroup(
            self, 
            "Application_Load_Balancer_Security_Group",
            vpc= vpc_webserver,
            description= "Security group of the Application Load Balancer",
            allow_all_outbound=True
        )
        alb_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(), 
            connection= ec2.Port.tcp(80), 
            description= "allow IPv4 HTTP access from the world"
        )
        alb_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(), 
            connection= ec2.Port.tcp(443), 
            description= "allow IPv4 HTTPS acccess from the world"
        )
        alb_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(80), 
            description= "allow IPv6 HTTP acccess from the world"
        )
        alb_sg.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(443), 
            description= "allow IPv6 HTTPS acccess from the world"
        )        
        alb_sg.add_ingress_rule(
            peer= ec2.Peer.ipv4("10.20.20.128/25"), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from Admin Server IP adress"
        )
        # ############### Roles & Policies ###############

        # # Instance role and SSM Managed Policy in order for SSH connection

        # SSM_role=iam.Role(
        #     self,  
        #     "InstanceSSM",
        #     assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        # )
        # SSM_role.add_managed_policy(
        #     iam.ManagedPolicy.from_aws_managed_policy_name(
        #         "AmazonSSMManagedInstanceCore"
        #     )
        # )
        # # Instance Role for S3 read access

        # S3_Access_role = iam.Role(
        #     self, 'S3_Access_role',
        #     assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
        #     managed_policies=[
        #         iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
        #         ],
        # )

        ############### Key Pair ###############

        # Key Pair Webserver

        self.web_keypair=ec2.CfnKeyPair(
            self,
            "Web_Keypair",
            key_name="Web_Keypair",
        )

        # Key Pair Admin Server

        self.admin_keypair=ec2.CfnKeyPair(
            self,
            "Admin_Keypair",
            key_name="Admin_Keypair",
        )

        ############### Key Management Service ###############

        ebs_admin_key=kms.Key(
            self, 
            "EBS_Admin_Key",
            enable_key_rotation = True,
            alias="EBS_Admin_Key",
            removal_policy=RemovalPolicy.DESTROY
            )
        # EBS_Web_Key=kms.Key(self, "EBS_Web_Key",
        #     enable_key_rotation=True,
        #     alias="EBS_Web_Key",
        #     removal_policy=RemovalPolicy.DESTROY
        #     )

        # self.vaultkey=kms.Key(
        #     self,  
        #     "vaultkey",
        #     enable_key_rotation=True,
        #     alias="Vault_Key",
        #     removal_policy=RemovalPolicy.DESTROY
        #     ),



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
            security_group=asg_sg,
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

        asg= autoscaling.AutoScalingGroup(
            self, 
            "Auto_Scaling_Group",
            vpc=vpc_webserver,
            auto_scaling_group_name="Auto_Scaling_Group",
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            # instance_type=ec2.InstanceType("t2.micro"),
            # machine_image=ec2.AmazonLinuxImage(),
            # key_name="Web_Keypair",
            launch_template=self.asg_launch_temp,
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
        asg.scale_on_cpu_utilization(
            "CPU_Auto_Scaling",
            target_utilization_percent=80
        )

        ############### EC2 Instance ###############

        # Instance2: Admin server

        self.adminserver=ec2.Instance(
            self, 
            "Adminserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            vpc=vpc_adminserver,
            availability_zone="eu-central-1b",
            instance_name= "Adminserver_Instance",
            security_group=adminserver_sg,
            key_name="Admin_Keypair",
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        30, 
                        encrypted=True,
                        kms_key=ebs_admin_key,
                        delete_on_termination=True
                    )
                )
            ]
        )


        ############### Webserver VPC Application Load Balancer ###############

        self.alb=elbv2.ApplicationLoadBalancer(
            self,
            "Application_Load_Balancer",
            vpc=vpc_webserver,
            security_group= alb_sg,
            internet_facing=True,
        )

        self.listener=self.alb.add_listener(
            "Listener",
            port=80
        )

        self.listener.add_targets(
            "ASG",
            port=80,
            targets=[asg],
            health_check=elbv2.HealthCheck(
                enabled=True,
                port="80"
            )
        )
        # # Redirect incoming traffic port 80 HTTP to port 443 HTTPS (HTTP to HTTPS is default setting)
        # self.ALB.add_redirect()

        # # Call the Certificate ARN
        # arn = 

        # # Call the Certificate
        # certificate = acm.Certificate.from_certificate_arn(self, "Certificate", arn)
        
        # # Listener for HTTPS
        # HTTPS_Listener= self.ALB.add_listener(
        #     'HTTPS_Listener',
        #     port=443,
        #     open=True,
        #     ssl_policy=elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
        #     # certificates=[certificate]
        # )

        # # Target Group for HTTPS Listener
        # asg_target_group=HTTPS_Listener.add_targets(
        #     'ASG',
        #     port=80,
        #     targets=[asg],
        #     health_check=elbv2.HealthCheck(
        #         enabled=True,
        #         port="80"
        #     ),
        #     stickiness_cookie_duration=Duration.minutes(5),
        #     stickiness_cookie_name="pbc"
        # )

        ############### S3 Bucket ###############

        # Create S3 bucket for bootstrap script

        scriptbucket=S3.Bucket(
            self,
            "scriptbucket",
            versioned=True,
            encryption=S3.BucketEncryption.S3_MANAGED,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Put userdata.sh from Script folder in S3 bucket

        s3deploy.BucketDeployment(
            self, 
            "BucketDeployment",
            destination_bucket=scriptbucket,
            sources=[s3deploy.Source.asset("./Scripts")]
        )

        # Allow EC2 instance to get files from the bucket

        # scriptbucket.grant_read(ASG.role)

        # ############### Script Launch ##############

        # script_path=Instance1.user_data.add_s3_download_command(
        #     bucket=scriptbucket,
        #     bucket_key="userdata.sh"
        # )

        # Instance1.user_data.add_execute_file_command(
        #     file_path=script_path
        # )

        script_path=asg.user_data.add_s3_download_command(
            bucket=scriptbucket,
            bucket_key="loadtest.sh"
        )

        asg.user_data.add_execute_file_command(
            file_path=script_path
        )


                ############### Backup Policies ###############

        # Create Tag

        Tags.of(asg).add("asg_tag", "asg_tag_value")

        # Create Backup Vault

        self.backup_vault=backup.BackupVault(
            self,
            "ASG_Backup_Vault",
            backup_vault_name="Backup_Vault",
            # encryption_key=self.vaultkey,
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create Backup Plan

        backupplan=backup.BackupPlan(
            self,
            "backupplan",
            backup_vault=self.backup_vault
        )

        # Add Resources to plan

        backupplan.add_selection(
            "Selection",
            resources=[
                backup.BackupResource.from_tag("asg_tag", "asg_tag_value")
            ]
        )

        # Add Backup Rule: each day at 00:00 with 7 days retention

        backupplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=self.backup_vault,
                rule_name="Daily_Backup_7_Day_Retention",
                schedule_expression=events.Schedule.cron(
                    week_day="*",
                    hour="0",
                    minute="0"
                    ),
                delete_after=Duration.days(7),
            )
        )

        # recovery point time 24 hours
        # recovery speed ASAP
