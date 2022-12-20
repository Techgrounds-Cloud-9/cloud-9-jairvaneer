____

# Log [date]

## One Sentence summary of the day

## Challenges

## Solutions


____

# Log [date]

## One Sentence summary of the day

## Challenges

## Solutions

____

# Log [date]

## One Sentence summary of the day

## Challenges

## Solutions

____

# Log 20/12/2022

## One Sentence summary of the day
Started with Auto Scaling Group and Application Load Balancer.
## Challenges
Should the ASG replace the webserver, and should the instance scale horizontally in multiple AZ's to increase failover security?
## Solutions
No solutions yet, probably trying out whether it is achievable to scale over multiple AZ's without rising costs.
____

# Log 19/12/2022

## One Sentence summary of the day
Started V1.1 documentation and stack.
## Challenges
How to implement the demands of the client.
## Solutions
Researching the AWS services that can be used to fulfill the demands and crreate the desired infrastructure.
____

# Log 16/12/2022

## One Sentence summary of the day
Finished V1.0, except one minor detail.
## Challenges
How to make an SSH connecting from the Admin server to the Web server without storing the private access keys on the admin server?
## Solutions
T.B.D. Currently looking into data transfer via RDP, where I can read data stored on the local machine without storing it on the admin server.
____

# Log 15/12/2022

## One Sentence summary of the day
Final tests, creating a PostDeploymentScript Bucket and seeing everything runs smoothly, working on documentation.
## Challenges

## Solutions
____

# Log 14/12/2022

## One Sentence summary of the day
Working on the last few components of the infrastructure.
## Challenges
Problems with UserData and Ephemeral Ports for the Network ACL.
## Solutions
Created Ingress/Egress rules for the Ephemeral Ports and rewrote the user data for the webserver.
____

# Log 13/12/2022

## One Sentence summary of the day
Fixed the run problem, currently working out the kinks in the Network ACL.
## Challenges
Not able to make connections to the Admin server via ssh/rdp when using the Network ACL, despite having configured ports 22 (SSH) and 3389 (RDP).
## Solutions
Opening up the ephemeral ports (1054, 65535) solved the problem.
____

# Log 12/12/2022

## One Sentence summary of the day
Working on an EC2 run problem.
## Challenges
Found that the Ec2 webserver instance kept on stopping instead of running smoothly.
## Solutions
First, commented everything in the stack but the VPC and the Instances and deployed. This showed the instances running successfully, so then I started destroying the app, adding a component to the stack by uncommenting it, and the redeploying. By methodically ruling out components of the infrastructure that were connected to the instance, I found out the problem was the EBS Block Device.
____

# Log 09/12/2022

## One Sentence summary of the day
Presented on progress.
## Challenges
How to portray my progress in a clear and concise manner?
## Solutions
By having clear documentation on my progress (Time Logs), the demands and assumtions made at the start of the project, and by having a clear structure in the code stack.
____

# Log 08/12/2022

## One Sentence summary of the day
Worked on the userdata script.
## Challenges
How to add the user data script to the bucket.
## Solutions
By creating a seperate folder in the the cdkproject directory and placing the userdata.sh file in there, and then specifying the path to it, I was able to add the userdata to the bucket.
____


# Log 07/12/2022

## One Sentence summary of the day
Today I started with working on the VPC Peering, as I needed some time to think about the user data scripts
## Challenges
I was unsuccesfull in finding a way to get the userdata read from the S3 bucket. I tried putting it in as a .zip file, but was informed that that was not the solution during the scrum master meeting.
## Solutions

____

# Log 06/12/2022

## One Sentence summary of the day
Started working on the S3 bucket
## Challenges
How to configure the S3 bucket as wanted, and how to get the user data script in there.
## Solutions
The bucket configuration is successfull, User data scripts is for another day.
____

# Log 05/12/2022

## One Sentence summary of the day
Finished the Stack containing the VPC's, Network ACL's and Security Groups
## Challenges
Specifying the exact inbound/outbound rules for the required protocols took longer than expected.
## Solutions
Asked for clarification on all relevant inbound/outbound requirements and finished the necessary rules.
____

# Log 02/12/2022

## One Sentence summary of the day
Defined the NetworkACL and started on the security groups.
## Challenges
Learning abbout the necessary properties for the NACL took some time.
## Solutions
Keeping notes on the information provided online gave me a clearer overview of the necessary properties and configurations.
____

# Log 01/12/2022

## One Sentence summary of the day
Succeeded in creating the Stack for the VPC's, started adding NetworkACL configuration.
## Challenges
The infrastructure for the assignment was stil a bit unclear.
## Solutions
We had our product owner meeting today and Shikha answered our questions on the infrastructure.
____

# Log 30/11/2022

## One Sentence summary of the day
Started with creating the VPC for the infrastructure.
## Challenges
Unnsure on how to use the CDK still.
## Solutions
Learning by doing with regards to the AWS CDK.
____

# Log 29/11/2022

## One Sentence summary of the day
Installed all the necessary components to start using AWS CDK.
## Challenges
Encountered a number of errors when trying to install CDK, CLI and Node.js
## Solutions
Took me quite a few hours, but after researching the problems thoroughly I was able to install the necessary programs and create a new directory for the CDK Project.
____

# Log 28/11/2022

## One Sentence summary of the day
Worked on the exploration epic, identifying the demands of the client and what logical assumptions about the cloud infrastructure followed those demands, as well as provisioning a list of the services needed for the infrastructure.
## Challenges
We didn't know why a specific server had to be placed in a seperate region. This caused some discussion in the group.
## Solutions
Upon closer inspection, it turned out to be a deliberate design flaw. In our cloud infrastructure, it is best practice to not place that specific structure in a seperate region.