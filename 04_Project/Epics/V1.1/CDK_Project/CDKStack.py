"""
CDK-Project V1.1

Infrastructure requirements:
1 Region
2 VPC's, each with 2 public subnets

VPC Peering Connection

VPC Webserver:                   
    1 public subnets, 3 private subnets (10.10.10.0/24)
    Using ALB as load balancer and as proxy
    ALB also changes HTTP connections to HTTPS with TLS 1.2 or better, need for Cerftificate manager
    1 EC2 Instance (Linux) in private subnet, ALB in public subnet replacing webserver v1.0 -> no public IP
    Auto-scaling group for private subnets, max 3 webservers
    AMI new VM's from snapshot current webserver
    1 Network ACL allowing HTTP/HTTPS from everywhere, SSH from admin server
    
    1 Webserver Security Group
    Daily backup with 7 days retention
    Schedule Health Checks -> failing leads to auto recovery

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


from  urllib import response
import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2, 
    aws_iam as iam, 
    aws_backup as backup,
    aws_ssm as ssm,
    aws_s3 as S3,
    aws_s3_deployment as s3deploy,
    aws_kms as kms,
    aws_events as event,
    RemovalPolicy,
    Duration,
    CfnOutput,
    App,
    Tags,
    Stack
)

from constructs import Construct
from aws_cdk.aws_events import Schedule
from aws_cdk.aws_s3_assets import Asset

# Stack

class CDKStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        ############### Create 2 VPC's & VPC Peering ###############

        # VPC 1 - Webserver VPC

        VPC1=ec2.Vpc(
            self, 
            "WebserverVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            vpc_name="WebserverVPC",
            availability_zones=["eu-central-1a", "eu-central-1b"],
            nat_gateways=0,
            # Configure 1 subnet in each AZ 
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public_subnet", 
                    cidr_mask=25, 
                    subnet_type=ec2.SubnetType.PUBLIC
                    )
            ]
        )

        # VPC 2 - Adminserver VPC

        VPC2=ec2.Vpc(
            self, 
            "AdminserverVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            vpc_name="AdminserverVPC",
            availability_zones=["eu-central-1a", "eu-central-1b"],
            nat_gateways=0,
            # Configure 1 subnet in each AZ
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public_subnet", 
                    cidr_mask=25, 
                    subnet_type=ec2.SubnetType.PUBLIC),
            ]
        )

        # VPC Peering

        VPC_Peering_Connection=ec2.CfnVPCPeeringConnection(
            self, 
            "VPC1_VPC2_Peering_Connection",
            peer_vpc_id=VPC2.vpc_id,
            vpc_id=VPC1.vpc_id,
        )
        
        # VPC Peering connection from VPC2 to VPC1 through Route Table 

        Admin_to_Web_Route=ec2.CfnRoute(
            self,
            "Admin_to_Web_Route",
            route_table_id=VPC2.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=VPC1.vpc_cidr_block,
            vpc_peering_connection_id=VPC_Peering_Connection.ref,
        )

        # VPC Peering connection from VPC1 to VPC2 through Route Table 

        Web_to_Admin_Route=ec2.CfnRoute(
            self,
            "Web_to_Admin_Route",
            route_table_id=VPC1.public_subnets[0].route_table.route_table_id,
            destination_cidr_block=VPC2.vpc_cidr_block,
            vpc_peering_connection_id=VPC_Peering_Connection.ref,
        )


        ############## Network ACL's ###############

        # Network ACL Webserver

        NACL1=ec2.NetworkAcl(
            self, 
            "WebServer_NACL",
            vpc= VPC1,
            network_acl_name="Webserver_NACL",
            subnet_selection=ec2.SubnetSelection(
                availability_zones=["eu-central-1a"],
                )
        )
        NACL1.add_entry("Allow_All_Ingress_IPv4_HTTP_to_Webserver",
            cidr= ec2.AclCidr.any_ipv4(),
            rule_number= 100,
            traffic= ec2.AclTraffic.tcp_port(80),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        NACL1.add_entry("Allow_All_Ingress_IPv6_HTTP_to_Webserver",
            cidr= ec2.AclCidr.any_ipv6(),
            rule_number= 140,
            traffic= ec2.AclTraffic.tcp_port(80),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        NACL1.add_entry("Allow_All_Ingress_IPv4_HTTPS_to_Webserver",
            cidr= ec2.AclCidr.any_ipv4(),
            rule_number= 110,
            traffic= ec2.AclTraffic.tcp_port(443),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        NACL1.add_entry("Allow_All_Ingress_IPv6_HTTPS_to_Webserver",
            cidr= ec2.AclCidr.any_ipv6(),
            rule_number= 110,
            traffic= ec2.AclTraffic.tcp_port(443),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        NACL1.add_entry("Allow_Ingress_SSH_from_Adminserver",
            cidr= ec2.AclCidr.ipv4("10.20.20.128/25"),
            rule_number= 120,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )                        
        NACL1.add_entry("Allow_Ingress_Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=130,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS, 
            rule_action=ec2.Action.ALLOW,
        )
        NACL1.add_entry("Allow_All_Egress",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS, 
            rule_action=ec2.Action.ALLOW,
        )

        # # Network ACL Admin Server

        NACL2 = ec2.NetworkAcl(
            self, 
            "Adminserver_NACL", 
            vpc = VPC2,
            network_acl_name="Adminserver_NACL",
            subnet_selection=ec2.SubnetSelection(
                availability_zones=["eu-central-1b"],
                )
        )
        NACL2.add_entry("Allow_Admin_Ingress_SSH_to_Adminserver",
            cidr= ec2.AclCidr.ipv4("178.85.64.168/32"),
            rule_number= 100,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        NACL2.add_entry("Allow_Admin_Ingress_RDP_to_Adminserver",
            cidr= ec2.AclCidr.ipv4("178.85.64.168/32"),
            rule_number= 110,
            traffic= ec2.AclTraffic.tcp_port(3389),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )  
        NACL2.add_entry("Allow_Admin_Ingress_RDP_to_Adminserver_IPv6",
            cidr=ec2.AclCidr.any_ipv6(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )
        NACL2.add_entry("Allow_Ingress_Ephemeral_from_Webserver",
            cidr=ec2.AclCidr.ipv4("10.10.10.0/25"),
            rule_number=130,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS, 
            rule_action=ec2.Action.ALLOW,
        )
        NACL2.add_entry("Allow_All_Egress",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS, 
            rule_action=ec2.Action.ALLOW,
        )

        ############### Security Groups ###############

        # Security Group Webserver

        Webserver_SG = ec2.SecurityGroup(
            self, 
            "Webserver_Security_Group",
            vpc= VPC1,
            description= "Security group of the Webserver",
            allow_all_outbound=True
        )
        Webserver_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(), 
            connection= ec2.Port.tcp(80), 
            description= "allow IPv4 HTTP access from the world"
        )
        Webserver_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv4(), 
            connection= ec2.Port.tcp(443), 
            description= "allow IPv4 HTTPS acccess from the world"
        )
        Webserver_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(80), 
            description= "allow IPv6 HTTP acccess from the world"
        )
        Webserver_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(443), 
            description= "allow IPv6 HTTPS acccess from the world"
        )
        Webserver_SG.add_ingress_rule(
            peer= ec2.Peer.ipv4("10.20.20.128/25"), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from Admin Server IP adress"
        )

        # Security Group Admin Server

        Adminserver_SG = ec2.SecurityGroup(
            self, 
            "Adminserver_Security_Group",
            vpc=VPC2,
            description= "Security group of the Adminserver",
            allow_all_outbound=True
        )
        Adminserver_SG.add_ingress_rule(
            peer= ec2.Peer.ipv4("178.85.64.168/32"), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from admin IPv4 adress"
        )
        Adminserver_SG.add_ingress_rule(
            peer= ec2.Peer.ipv4("178.85.64.168/32"), 
            connection= ec2.Port.tcp(3389), 
            description= "allow RDP access from admin IPv4 adress"
        )
        Adminserver_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(3389), 
            description= "allow RDP access from admin IPv6 adress"
        )        
        Adminserver_SG.add_ingress_rule(
            peer= ec2.Peer.any_ipv6(), 
            connection= ec2.Port.tcp(22), 
            description= "allow SSH access from admin IPv6 adress"
        )

        # ############### Roles & Policies ###############

        # Instance role and SSM Managed Policy in order for SSH connection

        SSM_role=iam.Role(
            self,  
            "InstanceSSM",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        SSM_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )
        # Instance Role for S3 read access

        S3_Access_role = iam.Role(
            self, 'S3_Access_role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
        )

        ############### Key Pair ###############

        # Key Pair Webserver

        Web_Keypair=ec2.CfnKeyPair(
            self,
            "Web_Keypair",
            key_name="Web_Keypair",
            tags=[{"key":"name", "value":"web-key"}]
        )

        # Key Pair Admin Server

        Admin_Keypair=ec2.CfnKeyPair(
            self,
            "Admin_Keypair",
            key_name="Admin_Keypair",
            tags=[{"key":"name", "value":"admin-key"}]
        )

        ############### Key Management Service ###############

        Bucket_Key=kms.Key(self, "Bucket_Key",
            enable_key_rotation=True,
            alias="Bucket_Key",
            removal_policy=RemovalPolicy.DESTROY
            )
        EBS_Admin_Key=kms.Key(self, "EBS_Admin_Key",
            enable_key_rotation = True,
            alias="EBS_Admin_Key",
            removal_policy=RemovalPolicy.DESTROY
            )
        EBS_Web_Key=kms.Key(self, "EBS_Web_Key",
            enable_key_rotation=True,
            alias="EBS_Web_Key",
            removal_policy=RemovalPolicy.DESTROY
            )
        Vault_Key=kms.Key(self, "Vault_Key",
            enable_key_rotation=True,
            alias="Vault_Key",
            removal_policy=RemovalPolicy.DESTROY
            )

        # ############### EC2 Instances ###############

        # Instance: Web server (Linux)

        Instance1=ec2.Instance(
            self, 
            "WebserverEC2",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=VPC1,
            availability_zone="eu-central-1a",
            instance_name="Webserver_Instance",
            role=S3_Access_role,
            security_group=Webserver_SG,
            key_name="Web_Keypair",
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        30, 
                        encrypted=True,
                        kms_key=EBS_Web_Key,
                        delete_on_termination=True
                    )
                )
            ]
        )

        # # Instance2: Admin server

        Instance2=ec2.Instance(
            self, 
            "Adminserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            vpc=VPC2,
            availability_zone="eu-central-1b",
            instance_name= "Adminserver_Instance",
            role=SSM_role,
            security_group=Adminserver_SG,
            key_name="Admin_Keypair",
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        30, 
                        encrypted=True,
                        kms_key=EBS_Admin_Key,
                        delete_on_termination=True
                    )
                )
            ]
        )

        # ############### S3 Bucket ###############

        # Create S3 bucket for bootstrap script

        scriptbucket=S3.Bucket(
            self,
            "scriptbucket",
            versioned=True,
            encryption=S3.BucketEncryption.S3_MANAGED,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Put cdkproject folder in S3 bucket

        s3deploy.BucketDeployment(
            self, 
            "BucketDeployment",
            destination_bucket=scriptbucket,
            sources=[s3deploy.Source.asset("./Scripts")]
        )

        # Allow EC2 instances to get files from the bucket

        scriptbucket.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[iam.ServicePrincipal("ec2.amazonaws.com")],
                actions=["s3:GetObject"],
                resources=[f"{scriptbucket.bucket_arn}/*"])
        )

        # ############### Script Launch ##############

        script_path=Instance1.user_data.add_s3_download_command(
            bucket=scriptbucket,
            bucket_key="userdata.sh"
        )

        Instance1.user_data.add_execute_file_command(
            file_path=script_path
        )

        # ############### Backup Policies ###############


        # Backup Webserver
        # Create Backup Vault

        webservervault=backup.BackupVault(
            self,
            "Webserver_Backup_Vault",
            encryption_key=Vault_Key,
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create Backup Plan

        webserverplan=backup.BackupPlan(
            self,
            "webserver_backup_plan",
        )

        # Add Resources to plan

        webserverplan.add_selection("Selection",
        resources=[
            backup.BackupResource.from_ec2_instance(Instance1)
        ]
        )

        # Add Backup Rule: each day at 00:00 with 7 days retention

        webserverplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=webservervault,
                rule_name="Daily_Backup_7_Day_Retention",
                schedule_expression=Schedule.cron(
                    week_day="*",
                    hour="17",
                    minute="0"
                    ),
                delete_after=Duration.days(7),
            )
        )