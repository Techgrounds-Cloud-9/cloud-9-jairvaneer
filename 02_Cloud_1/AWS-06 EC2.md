# EC2
The AWS service that is used to run virtual machines. Using this service to do so is called an instance.
## Key terminology
- **VM**  
See LNX-01.
- **SSH**  
See LNX-01.
- **RDP**  
Short for Remote Desk Protocol. It's a Microsoft protocol for using a computer remotely, or through a Virtual Machine (VM).  
- **AMI**  
Short for Amazon Machine Image. An AMI is a supported and maintained image that contains all the informaton to launch an instance. Therefore, to launch an instance, you don't have to configure all the settings yourself within AWS but can instead use these blueprints.
- **EBS**  
Short for Elastic Block Storage. Also known as persistent storage.
- **Instance Store**  
This is ephemeral storage.  
- **Security Group**  
This is a stateful firewall that works using explicit allow rules. By using the Security Group service, you don’t have to worry about firewalls on the OS level.  
- **User Data**  
With this, you can specify a (bash) script that runs on boot, allowing for easy configuration of the servers.
## Exercise
### Sources
- https://www.cloudflare.com/learning/access-management/what-is-the-remote-desktop-protocol/  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminate-serial-console-session.title.html

### Overcome challenges
- I didn't know whether I had to terminate the instance from the ssh client or from the EC2 dashboard. But that was a minor hurdle, and I cleared this with Shikha.

### Results
- Launched an EC2 instance.  
![lauch instance](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e7675a26f420dd111e660d215d8ed5ada528af8e/00_includes/Sprint%204/Screenshots%20AWS/AWS-06/AWS-06%20Exercise%201%20-%20%231_Launch_Instance.png)
- Passed the status checks.  
![status checks](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e7675a26f420dd111e660d215d8ed5ada528af8e/00_includes/Sprint%204/Screenshots%20AWS/AWS-06/AWS-06%20Exercise%202%20-%20%231_Status_Checks_Passed.png)
- Logged in to and out of the instance using an ssh connection.  
![Log in and out](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e7675a26f420dd111e660d215d8ed5ada528af8e/00_includes/Sprint%204/Screenshots%20AWS/AWS-06/AWS-06%20Exercise%202%20-%20%232_Logged_In_and_Closed.png)
- Terminated the instance from the dashboard.  
![Terminated Instance](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/e7675a26f420dd111e660d215d8ed5ada528af8e/00_includes/Sprint%204/Screenshots%20AWS/AWS-06/AWS-06%20Exercise%202%20-%20%233_Terminated_Instance.png)  