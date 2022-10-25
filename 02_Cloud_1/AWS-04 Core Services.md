# Core Services
This concerns the core services of AWS, those that are integral to the working of AWS and will appear on the exam.
## Key terminology
- **Amazon EC2**
See AWS-02.
- **AWS Lambda**  
AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. 
- **AWS Elastic Beanstalk**  
Elastic Beanstalk is a platform within AWS that is used for deploying and scaling web applications. In simple terms this platform as a service (PaaS) takes your application code and deploys it while provisioning the supporting architecture and compute resources required for your code to run. Elastic Beanstalk also fully manages the patching and security updates for those provisioned resources. 
- **Amazon VPC**  
Short for Amazon Virtual Private Cloud. It enables customers to launch AWS resources from a virtual network that they have defined. This network closely resembles a network hosted on a server, but makes use of all the benefits of the scalable infrastructure of AWS. Customers who opt for this model often have their own IT team specialized in AWS under contract. For more information on networks and their components, see IT Fundamentals 2: Networking.
- **Amazon Route 53**  
This is a scalable Domain Name System (DNS) service. AWS Route 53 translates URL names into their corresponding numeric IP addresses. IP addresses on the cloud can change frequently, as services move between data centers and physical machines. This means the translation and communication process is complex. Organizations that run machines in the cloud using Amazon Web Services (AWS) need an AWS DNS solution—a way to correctly translate user requests into Amazon IP addresses while adapting to cloud changes and quickly propagating them to DNS clients.Its name refers to both the classic highway US Route 66 and the destination for DNS server requests: TCP or UDP port 53. 
- **Amazon S3**
See AWS-02.
- **Amazon S3 Glacier**  
CLosely related to Amazon S3, Amazon S3 Glacier is used for archiving solutions. It is cheaper priced, but has more latency and less frequent access to data. It has two storage classes, Amazon S3 Glacier(intended for long-term storage that you don’t need to access quickly) and Amazon S3 Glacier Deep Archive (intended for extremely long-term archival with low access needs).
- **Amazon CloudFront**  
This is Amazons CDN (Content Delivery System) which is used for securely transferring content such as software, software development kits (SDK), videos and such to client with high transfer speed.
- **CDN**  
Short for Content Delivery Network. The term refers to a geographically distributed group of servers which work together to provide fast delivery of internet content. In other words, you use it to download stuff. It uses caching to reduce hosting bandwith, making it useful in improving website performance and elasticity.
- **Amazon RDS**
See AWS-01.
- **Amazon DynamoDB**  
This is an serverless hosted key-value NoSQL database designed to run applications. It is easily scalable, supports a high number of cryptographic libraries and has a simple API. It is designed to handle large scale SQL operations and JOINs without slowing down queries.  
- **JOIN**
In relational databases, such as SQL Server, Oracle, MySQL, and others, data is stored in multiple tables that are related to each other with a common key value. JOIN is an SQL clause used to query and access data from multiple tables, based on logical relationships between those tables.
- **API**  
Short for Application Programming Interface. This is a software intermediary that allows two applications to talk to one another.
- **NoSQL**  
Short for Not Only SQL. It is a type of database that that is non-tabular and stores data differently than relational tables. The main types a re document, key-value, wide-column and graph. They scale easily with large amounts of data and high user loads.  NoSQL databases allow developers to store huge amounts of unstructured data, giving them a lot of flexibility.
- **Amazon CloudWatch**  
This is an component of AWS that provides monitoring for AWS resources and the customer applications running on the Amazon infrastructure. CloudWatch enables real-time monitoring of AWS resources such as Amazon Elastic Compute Cloud (EC2) instances, Amazon Elastic Block Store (EBS) volumes, Elastic Load Balancing and Amazon Relational Database Service (RDS) instances. The application automatically collects and provides metrics for CPU utilization, latency and request counts. Users can also stipulate additional metrics to be monitored, such as memory usage, transaction volumes or error rates.
- **Amazon CloudFormation**  
CloudFormation is an infrastructure automation platform for AWS that deploys AWS resources in a repeatable, testable and auditable manner. By automating this process, it saves the customer time and rules out human error. It makes use of template files to automate the setup of resources. It can also be described as infrastructure automation or Infrastructure-as-Code (IaC) tool and a cloud automation solution because it can automate the setup and deployment of various Infrastructure-as-a-Service (IaaS) offerings available on AWS as CloudFormation supports virtually every service that runs in AWS.
- **AWS Identity and Access Management**  
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources. Just like any network, it has a root user which can be used to create different user profiles with their own set of permissions.  
- **Well-Architected Framework**
- **Cloud Pricing Model**

## Exercise
### Sources
- https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf  
- https://aws.amazon.com/lambda/  
- https://aws.amazon.com/elasticbeanstalk/  
- https://www.hava.io/blog/what-is-aws-elastic-beanstalk  
- https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html  
- https://avinetworks.com/glossary/aws-route-53/  
- https://www.msp360.com/resources/blog/amazon-s3-glacier/  
- https://tutorialsdojo.com/amazon-s3-vs-glacier/  
- https://www.simplilearn.com/tutorials/aws-tutorial/aws-cloudfront  
- https://www.cloudflare.com/learning/cdn/what-is-a-cdn/  
- https://aws.amazon.com/dynamodb/  
- https://www.mongodb.com/nosql-explained
- https://www.mulesoft.com/resources/api/what-is-an-api  
- https://www.devart.com/dbforge/sql/sqlcomplete/sql-join-statements.html  
- https://www.techtarget.com/searchaws/definition/CloudWatch  
- https://www.contino.io/insights/aws-cloudformation  
- 
### Overcome challenges
- No challenges, just learning.

### Results
- Studied the core concepts and the AWS Certified Cloud Practicioner (CLF-C01) Exam Guide.