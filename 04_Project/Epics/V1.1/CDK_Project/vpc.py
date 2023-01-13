import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

from CDK_Project.nacl import NACL_Construct
from CDK_Project.sg import  ALB_SG_Construct, ASG_SG_Construct, Admin_SG_Construct
from CDK_Project.s3 import S3_Construct
from CDK_Project.ec2 import Admin_Construct
from CDK_Project.asg import ASG_Construct
from CDK_Project.alb import ALB_Construct
from CDK_Project.backup import Backup_Construct


class VPC_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create Webserver VPC ###############

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

        ############### Create Adminserver VPC ###############

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

        self.admin_to_web_route=ec2.CfnRoute(
            self,
            "Admin_to_Web_Route",
            route_table_id=vpc_adminserver.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=vpc_webserver.vpc_cidr_block,
            vpc_peering_connection_id=vpc_peering_connection.ref,
        )

        ################ Network ACL Construct ################

        nacl=NACL_Construct(
            self,
            "Network_ACL_Construct",
            vpc_webserver=vpc_webserver,
            vpc_adminserver=vpc_adminserver
        )

        ################ Security Group Constructs ################

        alb_sg=ALB_SG_Construct(
            self,
            "Auto_Scaling_Group",
            vpc_webserver=vpc_webserver
        )
        asg_sg=ASG_SG_Construct(
            self, 
            "Security_Groups_Construct",
            vpc_webserver=vpc_webserver,
            )
        admin_sg=Admin_SG_Construct(
            self,
            "Auto_Scaling_Group",
            vpc_adminserver=vpc_adminserver
        )


        ################ Security Group Construct ################

        
        ################ Security Group Construct ################
        
        
        ################ Security Group Construct ################