# import aws_cdk as cdk
# from aws_cdk import (
#     aws_ec2 as ec2,
#     aws_iam as iam,
#     aws_ssm as ssm,
# )

# from constructs import Construct

# class RolesStack(cdk.NestedStack):
#     def __init__(self, scope: Construct, id: str, **kwargs) -> None:
#         super().__init__(scope, id, **kwargs)

#         # ############### Roles & Policies ###############

#         # Instance role and SSM Managed Policy in order for SSH connection

#         SSM_role=iam.Role(
#             self,  
#             "InstanceSSM",
#             assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
#         )
#         SSM_role.add_managed_policy(
#             iam.ManagedPolicy.from_aws_managed_policy_name(
#                 "AmazonSSMManagedInstanceCore"
#             )
#         )
#         # Instance Role for S3 read access

#         self.S3_Access_role = iam.Role(
#             self, 'S3_Access_role',
#             assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
#             managed_policies=[
#                 iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
#                 ],
#         )
