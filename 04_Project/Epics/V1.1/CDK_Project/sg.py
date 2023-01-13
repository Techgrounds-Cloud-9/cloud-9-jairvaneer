import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

my_ip="178.85.64.168/32"

        # Security Group Application Load Balancer Construct

class ALB_SG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

        # Security Group Auto Scaling Group Construct

class ASG_SG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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

        # Security Group Admin Server Construct

class Admin_SG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_adminserver, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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
