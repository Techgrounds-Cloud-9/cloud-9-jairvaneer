import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

my_ip="178.85.64.168/32"

class VPC_Stack(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create Webserver VPC ###############

        VPC_Webserver=ec2.Vpc(
            self, 
            "WebserverVPC",
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            vpc_name="WebserverVPC",
            availability_zones=["eu-central-1a", "eu-central-1b"],
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

        ############### Create Adminserver VPC ###############

        VPC_Adminserver=ec2.Vpc(
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

        VPC_Peering_Connection=ec2.CfnVPCPeeringConnection(
            self, 
            "VPC1_VPC2_Peering_Connection",
            peer_vpc_id=VPC_Adminserver.vpc_id,
            vpc_id=VPC_Webserver.vpc_id,
        )
        

                # VPC Peering connection from VPC1 to VPC2 through Route Table 

        self.Web_to_Admin_Route=ec2.CfnRoute(
            self,
            "Web_to_Admin_Route",
            route_table_id=VPC_Webserver.public_subnets[0].route_table.route_table_id,
            destination_cidr_block=VPC_Adminserver.vpc_cidr_block,
            vpc_peering_connection_id=VPC_Peering_Connection.ref,
        )

        # VPC Peering connection from VPC2 to VPC1 through Route Table 

        self.Admin_to_Web_Route=ec2.CfnRoute(
            self,
            "Admin_to_Web_Route",
            route_table_id=VPC_Adminserver.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=VPC_Webserver.vpc_cidr_block,
            vpc_peering_connection_id=VPC_Peering_Connection.ref,
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
