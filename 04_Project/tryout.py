        # ############### Roles & Policies ###############

        # Instance role and SSM Managed Policy in order for SSH connection

        # SSM_role=iam.Role(
        #     self,  
        #     "InstanceSSM",
        #     assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        # )
        # SSM_role.add_managed_policy(
        #     iam.ManagedPolicy.from_aws_managed_policy_name(
        #         "AmazonSSMManagedInstanceCore"
        #     )
        # )
        # Instance Role for S3 read access

        # S3_Access_role = iam.Role(
        #     self, 'S3_Access_role',
        #     assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
        #     managed_policies=[
        #         iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
        #         ],
        # )

                # # Allow EC2 instances to get files from the bucket

        # scriptbucket.add_to_resource_policy(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.ALLOW,
        #         principals=[iam.ServicePrincipal("ec2.amazonaws.com")],
        #         actions=["s3:GetObject"],
        #         resources=[f"{scriptbucket.bucket_arn}/*"])
        # )