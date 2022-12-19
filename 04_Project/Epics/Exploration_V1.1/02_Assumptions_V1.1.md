# What assumptions have I made?
### **It should no longer be possible to approach the webserver "naked" over he internet. The customer would like to see a proxy installed. Additionally, the server should no longer have a public IP adress.**  
Use an ALB to install a proxy server in a public subnet, place the webserver in a private subnet. Use a NAT gateway to connect to the internet.
### **If a user connects to the load balancer via HTTP, the connection should be automatically upgraded to HTTPS.**
Set rules in the ALB for this to happen.
### **In such an event, the connection should be encrypted by use of TLS 1.2 or higher.**
Install and configure Certificate Manager.
### **The webserver should be health checked in frequent intervals.**
Create a Lambda function that triggers these health checks (Checker_fn), for timing use Amazon Cloudwatch Events.
### **Should the webserver fail this health check, than it should automatically be restored.**
Another lambda function depending on the result of the first. If health check fails, the virtual IP adress should be moved to a backup server. So a backup server is needed at all times in a different availability zone.
### **If its the case that the webserver is placed under continuous load, a temporary extra server should be provisioned. The client thinks he will never need more than threee servers, given his past user numbers.**
Use auto scaling groups with set rules concerning when to start additional instances, and where to place them (availability zones).