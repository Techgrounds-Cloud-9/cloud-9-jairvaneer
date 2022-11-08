# VPC
Short for Virtual Privayte CLoud. This is a virtual private data center in the cloud. This network is isolated from other networks. With a VPC you have full control over the design of the network, as you control the creation of subnets, internet gateways (IGW), NAT gateways, VPN connections and more.  
In a standard AWS account, you can have up to 5 VPCs. Many services, like, EC2, RDS and ECS require a VPC o be placed into. Therefore, when creating an account, a default VPC is also created.  When you create a VPC, you must assign a CIDR block. Choose your CIDR block and subnet mask carefully, as they have to allow for enough subnets and hosts and cannot be changed after creation.

Subnets can be either public or private. The only difference is that private subnets do not have an entry for the internet gateway (igw) in their route table, where public subnets do. In other words, private subnets cannot access the internet without a NAT gateway or a NAT instance.

VPCs operate at the regional level, while subnets can only be placed into a single Availability Zone.

Elastic IPs are also available from the VPC menu. EIPs are public IP addresses that can be dynamically allocated to resources like EC2 instances or NAT gateways.

## Key terminology


## Exercise
### Sources
- https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html
- https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#DefaultSecurityGroup  
- https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/authorizing-access-to-an-instance.html  
- https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html  


### Overcome challenges
- There is no VPC Launch Wizard, so had to do it another way.
- When connecting to the instance it took me quite some time to remember that I needed to input "http" before the IPv4 adress, because the default is "https", but we did not gave inbound permission for those.
### Results
- Allocated an Elastic IP Address to my account.  
![Allocated EIP](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e81df421f9f41272b6afc8aec7b430d7c6fc04f3/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%201%20-%20%231_Allocate_EIP.png)
- Created a new VPC.  
![Created VPC](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e81df421f9f41272b6afc8aec7b430d7c6fc04f3/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%201%20-%20%232_VPC.png)
- Created additional subnets.  
![Created subnets](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e81df421f9f41272b6afc8aec7b430d7c6fc04f3/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%202%20-%20%231_Subnets.png)
- Renamed the route tables.  
![Renamed route tables](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/15fd898fe823f0ae750c5671ba39597e10621ef4/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%202%20-%20%232_Public_Route_Table.png)
- Associated the subnets to the route tables.  
![Associated subnets](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/15fd898fe823f0ae750c5671ba39597e10621ef4/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%202%20-%20%233_Subnet_Associations.png)  
- Created the Security Group.  
![Created Security Group](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e81df421f9f41272b6afc8aec7b430d7c6fc04f3/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%203%20-%20%231_Security_Group.png)
- Launched an EC2 instance.  
![Launched instance](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e81df421f9f41272b6afc8aec7b430d7c6fc04f3/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%204%20-%20%231_Connect_Using_Public_DNS.png)
- Conneted to the instance using the public IPv4 DNS name.  
![Connected to instance](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e81df421f9f41272b6afc8aec7b430d7c6fc04f3/00_includes/Sprint%204/Screenshots%20AWS/AWS-10/AWS-10%20Exercise%204%20-%20%231_Launch_EC2_Instance.png)
