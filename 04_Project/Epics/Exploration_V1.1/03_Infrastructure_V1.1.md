# Overview of the necessary Cloud Infrastructure
# Overview of the necessary Cloud Infrastructure
* **VPC's:** Two in total, same region. Webserver VPC has one public subnet, two private subnets. ALB will be in public, webserver instance in private subnet 1, backup instance in private subent 2. Adminserver VPC has a public subnet
* **VPC Peering:** To establish secure connection between the VPC's.
* **EC2 instances:** Two in total, one webserver, one admin server.   
* **Security group:** Custom traffic rules for the different instances, one set for the webserver and one set for the management server.  
* **Network ACL:** Custom traffic rules for the different subnets, with all HTTP/HTTPS connections open for the webserver subnet and some connections open for the admin instance subnet.  
* **IAM:** Used to create users and assign roles. We will need roles for the use of the SSM and for the Ec2 instances to read a seperate S3 bucket.
* **AWS Backup:** Create a backupvault for the data from the webserver. Daily backups with 7 days retention. 
* **KMS:** Central place for the creation and management of encryption keys. These are needed to encrypt the back up data and the EC2 instances.  
* **S3 bucket:** A new S3 bucket for the userdata script post deployment. 
* **EC2 Auto-Scaling:** We use Auto-Scaling to ensure that the webserver scales automatically and horizontally when the traffic reaches a certain threshold. Max instances = 3.
* **Application Load Balancer** We use an Application Load Balancer to make sure that the load is evenly distributed in the event of multiple instances running side-by-side. Also, we can use this as a proxy that sits between our users and our webserver, which is placed in a private subnet.