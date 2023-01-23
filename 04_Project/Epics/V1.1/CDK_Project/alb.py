from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2
)

from constructs import Construct

        ############### Application Load Balancer ###############


class ALB_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, asg:autoscaling.AutoScalingGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        alb=elbv2.ApplicationLoadBalancer(
            self,
            'Application_Load_Balancer',
            vpc=vpc,
            internet_facing=True,
        )

        # listener=alb.add_listener(
        #     "Listener_for_HTTP",
        #     port=80,
        #     open=True
        # )

        # asg_target_group=listener.add_targets(
        #     "ASG Webserver",
        #     port=80,
        #     targets=[asg],
        #     health_check=elbv2.HealthCheck(
        #         enabled=True,
        #         port="80"
        #     )
        # )

        # asg.connections.allow_to(asg_target_group, connection_type)

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
