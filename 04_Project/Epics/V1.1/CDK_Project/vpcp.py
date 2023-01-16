import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

class VPC_Peering_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc1: ec2.Vpc, vpc2: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### VPC Peering ###############

        vpc_peering_connection=ec2.CfnVPCPeeringConnection(
            self, 
            "VPC1_VPC2_Peering_Connection",
            peer_vpc_id=vpc2.vpc_id,
            vpc_id=vpc1.vpc_id,
        )
        

        # VPC Peering connection from VPC1 to VPC2 through Route Table 

        for i in range(0, 1):
            self.web_to_admin_route=ec2.CfnRoute(
                self,
                "Web_to_Admin_Route",
                route_table_id=vpc1.public_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc2.vpc_cidr_block,
                vpc_peering_connection_id=vpc_peering_connection.ref,
            )

        # VPC Peering connection from VPC2 to VPC1 through Route Table 

        for i in range(0, 1):
            self.admin_to_web_route=ec2.CfnRoute(
                self,
                "Admin_to_Web_Route",
                route_table_id=vpc2.public_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc1.vpc_cidr_block,
                vpc_peering_connection_id=vpc_peering_connection.ref,
            )