# This IaC code contains the complete network stack and all its components
# The first part wil provision the VPC with two public subnets
# After this the components will be added

vpc = ec2.Vpc(
        self, "JairVpc"
        cidr="10.10.10.0/24"
        max_azs=2
        nat_gateways=0
        subnet_configuration= [
            ec2.SubnetConfiguration(name="public", cidr_mask=24, subnet_type=ec2.SubnetType.Public)
        ]
)
