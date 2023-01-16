#####################################################
############## Network ACL Constructs ###############
#####################################################

from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

my_ip="178.85.64.168/32"

# Network ACL Webserver Construct

class NACL_Web_Construct(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        nacl_web=ec2.NetworkAcl(
            self, 
            "WebServer_NACL",
            vpc=vpc,
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

# Network ACL Admin Server Construct

class NACL_Admin_Construct(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        nacl_admin = ec2.NetworkAcl(
            self, 
            "Adminserver_NACL", 
            vpc = vpc,
            network_acl_name="Adminserver_NACL",
            subnet_selection=ec2.SubnetSelection(
                availability_zones=["eu-central-1b"],
                )
        )
        nacl_admin.add_entry("Allow_Admin_Ingress_SSH_to_Adminserver_IPv4",
            cidr= ec2.AclCidr.ipv4(my_ip),
            rule_number= 100,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        nacl_admin.add_entry("Allow_Admin_Ingress_RDP_to_Adminserver_IPv4",
            cidr= ec2.AclCidr.ipv4(my_ip),
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