# Files, AppServices, CDN, DNS, Database
A number of services from AWS that we have to explore.
## Key terminology
- **Elastic Beanstalk**  
Amazon Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.  
Developers upload the application and Elastic Beanstalk takes care of all of the deployment detaisl. These include capacity provisioning, load balancing, auto-scaling and application health monitoring. WIth Elastic Beanstalk, you can use multiple availability zone to improve application reliability and availability.  
It is considered to be a Platform as a Service (PaaS) solution.
- **Amazon SQS**  
Short for Amazon Simple Queue Service. Its an hosted queue that lets you send, store and receive messages between software components.  
- **ASG**  
Short for Auto-Scaling Group. An Auto Scaling group contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. An Auto Scaling group also lets you use Amazon EC2 Auto Scaling features such as health check replacements and scaling policies. Both maintaining the number of instances in an Auto Scaling group and automatic scaling are the core functionality of the Amazon EC2 Auto Scaling service.  
- **Blue/Green Deployment**  
Blue green deployment is an application release model that gradually transfers user traffic from a previous version of an app or microservice to a nearly identical new release—both of which are running in production. 
The old version can be called the blue environment while the new version can be known as the green environment. Once production traffic is fully transferred from blue to green, blue can standby in case of rollback or pulled from production and updated to become the template upon which the next update is made.  
This is different from immutable updating of instances with Elastic Beanstalk, as with immutable the new instances are created under the same load balancer and serve traffic alongside one antoher before the old switches off, and with blue/green a new environment is created from scratch using a different load balancer, and the switch is performed at the DNS level routing the traffic from theold to the new.
- **Cloudfront**  
CloudFront is a web service that gives businesses and web application developers an easy and cost-effictive way to distribute content with low latency and high data transfer speeds. CloudFront is a good choice for distribution of frequently accessed static content that benefits from edge delivery, like popular website images, videos, media files or software downloads. Used for dynamic, static, streaming, and interactive content.
- **Route53**  
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) service. It offers domain name registry, DNS resolution and health checking of resouces.
- **EFS**  
Short for Elastic File System. Amazon EFS is a fully managed service for hosting Network File System (NFS) filesystems in the cloud.
It is an implementation of a NFS file share and is accessed using the NFS protocol.
It provides elastic storage capacity and pay for what you use (in contrast to Amazon EBS with which you pay for what you provision).
- **RDS**  
Short for Relational Database Service. This service helps you with launching and managing relational databases on AWS. It supports the following databases enigines: Amazon Aurora, MySQL, MariaDB, Oracle, SQL Server, PostgreSQL. Amazon RDS facilitates the deployment and maintenance of relational databases in the cloud. A cloud administrator uses Amazon RDS to set up, operate, manage and scale a relational instance of a cloud database. Amazon RDS is not itself a database; it is a service used to manage relational databases.
- **Aurora**
Amazon Aurora is a relational database management system (RDBMS) built for the cloud with full MySQL and PostgreSQL compatibility. Aurora gives you the performance and availability of commercial-grade databases at one-tenth the cost. It is part of Amazon RDS. It feutures are: Up to 5 times the throughput of MySQL and 3 times the throughput of PostgreSQL, up to 128TB of auto-scaling SSD storage, 6-way replication across three Availability Zones, up to 15 Read Replicas with sub-10ms replica lag and automatic monitoring and failover in less than 30 seconds
## Exercise
### Sources
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-roles.html?icmpid=docs_elasticbeanstalk_console  
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html  
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html  
- https://aws.amazon.com/route53/what-is-dns/  


### Overcome challenges
- No problems, just studying.

### Results
- Studied Elastic Beanstalk, CloudFront and Route53.  
- Used EFS in the console. Learned how to create a new EC2 instance which is connected to the file system, and how to connect an EC2 instance to an EFS via the CLI.
- Used RDS and Aurora in the console.