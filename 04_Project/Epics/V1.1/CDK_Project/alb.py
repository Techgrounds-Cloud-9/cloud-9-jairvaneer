import aws_cdk as cdk
from aws_cdk import (
    CfnOutput,
    Duration,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as acm,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling
)

from constructs import Construct


class ALB_Stack(cfn.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        VPC_Webserver=ec2.Vpc
        ALB_sg=ec2.SecurityGroup
        AS_Group=autoscaling.AutoScalingGroup

        ############### VPC1 Application Load Balancer ###############

        self.alb=elbv2.ApplicationLoadBalancer(
            self,
            'Application_Load_Balancer',
            vpc=VPC_Webserver,
            security_group= ALB_sg,
            internet_facing=True,
        )

        self.listener=self.alb.add_listener(
            "Listener",
            port=80
        )

        self.listener.add_targets(
            "ASG",
            port=80,
            targets=[AS_Group],
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
