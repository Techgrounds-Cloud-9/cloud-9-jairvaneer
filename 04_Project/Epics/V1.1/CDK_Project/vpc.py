import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    CfnOutput
)

from constructs import Construct

# from CDK_Project.nacl import NACL_Web_Construct, NACL_Admin_Construct
# from CDK_Project.sg import  ALB_SG_Construct, ASG_SG_Construct, Admin_SG_Construct
# from CDK_Project.s3 import S3_Construct
# from CDK_Project.ec2 import Admin_Construct
# from CDK_Project.asg import ASG_Construct
# from CDK_Project.alb import ALB_Construct
# from CDK_Project.backup import Backup_Construct


class VPC_Web_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create Webserver VPC ###############

        self.vpc_webserver=ec2.Vpc(
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

class VPC_Admin_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############### Create Adminserver VPC ###############

        self.vpc_adminserver=ec2.Vpc(
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

        # ############### VPC Peering ###############

        # vpc_peering_connection=ec2.CfnVPCPeeringConnection(
        #     self, 
        #     "VPC1_VPC2_Peering_Connection",
        #     peer_vpc_id=vpc_adminserver.vpc_id,
        #     vpc_id=vpc_webserver.vpc_id,
        # )
        

        #         # VPC Peering connection from VPC1 to VPC2 through Route Table 

        # self.web_to_admin_route=ec2.CfnRoute(
        #     self,
        #     "Web_to_Admin_Route",
        #     route_table_id=vpc_webserver.public_subnets[0].route_table.route_table_id,
        #     destination_cidr_block=vpc_adminserver.vpc_cidr_block,
        #     vpc_peering_connection_id=vpc_peering_connection.ref,
        # )

        # # VPC Peering connection from VPC2 to VPC1 through Route Table 

        # self.admin_to_web_route=ec2.CfnRoute(
        #     self,
        #     "Admin_to_Web_Route",
        #     route_table_id=vpc_adminserver.public_subnets[1].route_table.route_table_id,
        #     destination_cidr_block=vpc_webserver.vpc_cidr_block,
        #     vpc_peering_connection_id=vpc_peering_connection.ref,
        # )

        # ################ Network ACL Constructs ################

        # nacl_web=NACL_Web_Construct(
        #     self,
        #     "NACL_Webserver_Construct",
        #     vpc=vpc_webserver,
        # )
        # nacl_admin=NACL_Admin_Construct(
        #     self,
        #     "NACL__Adminserver_Construct",
        #     vpc=vpc_adminserver
        # )

#         ################ Security Group Constructs ################

#         # alb_sg=ALB_SG_Construct(
#         #     self,
#         #     "ALB_SG_Construct",
#         #     vpc=vpc_webserver
#         # )
#         # asg_sg=ASG_SG_Construct(
#         #     self, 
#         #     "ASG_SG_Construct",
#         #     vpc=vpc_webserver,
#         #     )
#         # adminserver_sg=Admin_SG_Construct(
#         #     self,
#         #     "Admin_Server_Security_Group_Construct",
#         #     vpc=vpc_adminserver
#         # )

#     #     class ALB_SG_Construct(Construct):

#     # def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
#     #     super().__init__(scope, construct_id, **kwargs)

#         alb_sg = ec2.SecurityGroup(
#             self, 
#             "Application_Load_Balancer_Security_Group",
#             vpc=vpc_webserver,
#             description= "Security group of the Application Load Balancer",
#             allow_all_outbound=True
#         )
#         alb_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv4(), 
#             connection= ec2.Port.tcp(80), 
#             description= "allow IPv4 HTTP access from the world"
#         )
#         alb_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv4(), 
#             connection= ec2.Port.tcp(443), 
#             description= "allow IPv4 HTTPS acccess from the world"
#         )
#         alb_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv6(), 
#             connection= ec2.Port.tcp(80), 
#             description= "allow IPv6 HTTP acccess from the world"
#         )
#         alb_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv6(), 
#             connection= ec2.Port.tcp(443), 
#             description= "allow IPv6 HTTPS acccess from the world"
#         )
#         alb_sg.add_ingress_rule(
#             peer= ec2.Peer.ipv4("10.20.20.128/25"), 
#             connection= ec2.Port.tcp(22), 
#             description= "allow SSH access from Admin Server IP adress"
#         )

#         # Security Group Auto Scaling Group Construct

# # class ASG_SG_Construct(Construct):

# #     def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
# #         super().__init__(scope, construct_id, **kwargs)

#         asg_sg = ec2.SecurityGroup(
#             self, 
#             "Auto_Scaling_Group_Security_Group",
#             vpc=vpc_webserver,
#             description= "Security group of the Auto Scaling Group",
#             allow_all_outbound=True
#         )
#         asg_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv4(), 
#             connection= ec2.Port.tcp(80), 
#             description= "allow IPv4 HTTP access from the world"
#         )
#         asg_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv4(), 
#             connection= ec2.Port.tcp(443), 
#             description= "allow IPv4 HTTPS acccess from the world"
#         )
#         asg_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv6(), 
#             connection= ec2.Port.tcp(80), 
#             description= "allow IPv6 HTTP acccess from the world"
#         )
#         asg_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv6(), 
#             connection= ec2.Port.tcp(443), 
#             description= "allow IPv6 HTTPS acccess from the world"
#         )
#         asg_sg.add_ingress_rule(
#             peer= ec2.Peer.ipv4("10.20.20.128/25"), 
#             connection= ec2.Port.tcp(22), 
#             description= "allow SSH access from Admin Server IP adress"
#         )

#         # Security Group Admin Server Construct

# # class Admin_SG_Construct(Construct):

# #     def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
# #         super().__init__(scope, construct_id, **kwargs)

#         adminserver_sg = ec2.SecurityGroup(
#             self, 
#             "Adminserver_Security_Group",
#             vpc=vpc_adminserver,
#             description= "Security group of the Adminserver",
#             allow_all_outbound=True
#         )
#         adminserver_sg.add_ingress_rule(
#             peer= ec2.Peer.ipv4("178.85.64.168/32"), 
#             connection= ec2.Port.tcp(22), 
#             description= "allow SSH access from admin IPv4 adress"
#         )
#         adminserver_sg.add_ingress_rule(
#             peer= ec2.Peer.ipv4("178.85.64.168/32"), 
#             connection= ec2.Port.tcp(3389), 
#             description= "allow RDP access from admin IPv4 adress"
#         )
#         adminserver_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv6(), 
#             connection= ec2.Port.tcp(3389), 
#             description= "allow RDP access from admin IPv6 adress"
#         )        
#         adminserver_sg.add_ingress_rule(
#             peer= ec2.Peer.any_ipv6(), 
#             connection= ec2.Port.tcp(22), 
#             description= "allow SSH access from admin IPv6 adress"
#         )



#         ################ S3 Bucket Construct ################

#         scriptbucket=S3_Construct(
#             self,
#             "Scriptbucket",
#             )

#         ################ Auto Scaling Group Construct ################

#         asg=ASG_Construct(
#             self,
#             "Auto_Scaling_Group_Construct",
#             vpc=vpc_webserver,
#             security_group=asg_sg,
#             s3_bucket=scriptbucket
#         )

#         ################ Admin Server Construct ################

#         adminserver=Admin_Construct(
#             self,
#             "Admin_Server_Construct",
#             vpc=vpc_adminserver,
#             security_group=adminserver_sg,
#         )

#         ################ Application Load Balancer Construct ################

#         alb=ALB_Construct(
#             self,
#             "ALB_Construct",
#             vpc=vpc_webserver,
#             security_group=alb_sg
#         )
#         ################ Backup Construct ################        

#         backup_plan=Backup_Construct(
#             self,
#             "Backup_Construct",
#             asg=asg
#         )
