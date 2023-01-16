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


        # # Create Vault Key

        # vaultkey=kms.Key(
        #     self,  
        #     "Vault_Key",
        #     enable_key_rotation=True,
        #     alias="Vault_Key",
        #     removal_policy=RemovalPolicy.DESTROY
        #     ),

            # encryption_key=vaultkey,