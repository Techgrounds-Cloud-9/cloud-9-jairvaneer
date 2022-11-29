# Overview of the necessary Cloud Infrastructure
* **EC2 instances:** Two in total, one webserver, one admin server.  
* **AWS Backup:** Service that creates and controls back ups, including frequency and retention.  
* **KMS:** Central place for the creation and management of encryption keys. These are needed to encrypt the back up data and the EC2 instances.  
* **S3 bucket:** Location of data and back up snapshots.  
* **Security group:** Custom traffic rules for the different instances, one set for the webserver and one set for the management server.  
* **Network ACL:** Custom traffic rules for the different subnets, with all HTTP/HTTPS connections open for the webserver subnet and some connections open for the admin instance subnet.  
* **IAM:** Used to create users and assign roles within the client's company. Depending on what the company wants, we create users for the staff and roles for the applications that need to connect to our instances.
* **Internet Gateway:** One needed, to connect to the internet. This connects the VPC  to the internet.
* **EC2 Auto-Scaling:** We use Auto-Scaling to ensure that the webserver scales automatically and horizontally when the load is to high for one instance.
* **Elastic Load Balancer** We use an elastic load balancer to make sure that the load is evenly distributed in the event of multiple instances running side-by-side. 
* **Route 53:** This is the Domain Name Service from AWS and it handles the routing of user requests to the right internet application, in our case the web server, running on AWS. This global service exists in the AWS Cloud.
