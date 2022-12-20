# What assumptions have I made?
### **It should no longer be possible to approach the webserver "naked" over he internet. The customer would like to see a proxy installed. Additionally, the server should no longer have a public IP adress.**  
Use an ALB to install a proxy server in a public subnet, place the webserver in a private subnet. Use a NAT gateway to connect to the internet.
### **If a user connects to the load balancer via HTTP, the connection should be automatically upgraded to HTTPS.**
Set rules in the ALB for this to happen.
### **In such an event, the connection should be encrypted by use of TLS 1.2 or higher.**
 We are not allowed to pay for the certificates, so we should make a self-signed certificate. However, these (like all certificates) are normally to an url rather than an IP adress, so we might have to use Route 53, the Domain Name Service of AWS, in order to register a domain and then get a self-signed certificate to that domain name by use of the certificate manager.
### **The webserver should be health checked in frequent intervals.**
ALB health checks takes are of the health checks, on a default interval of 30 secs.
### **Should the webserver fail this health check, than it should automatically be restored.**
EC2 auto scaling launches a new replacement instance if the health check is failed. 
### **If its the case that the webserver is placed under continuous load, a temporary extra server should be provisioned. The client thinks he will never need more than threee servers, given his past user numbers.**
Use auto scaling groups with set rules concerning when to start additional instances, and where to place them (availability zones).