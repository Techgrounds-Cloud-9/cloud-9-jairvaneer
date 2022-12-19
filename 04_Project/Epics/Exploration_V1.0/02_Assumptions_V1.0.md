# What assumptions have I made?
### **All VM disks need to be encrypted.**
In order to encrypt a VM (EC2 instance) we need to encrypt the EBS volume attached to the EC2 instance, or create the EC2 instance from an encrypted snapshot. This requires use of the KMS.
### **The webserver needs daily back-ups. These back-ups need to be saved for 7 days.**
Configure AWS Back Ups with a custom back up plan that takes a daily back up of the web server and place this in a back up vault. Possibly needed to create our own back up vault.  
The back up should be automatically deleted after 7 days. This is done under retention management.  
There is no need for cross-region back-ups so the back-up will be in the same region as the webserver, but not in the same availability zone.  
Make sure the user data is also backed-up.  
It is needed to install an AWS Backup Gateway and connect it to the hypervisor so that any additionally created VM's when the load grows are also baked up.
### **Automate deployment of webserver.**
Use EC2 user data to install all packages, configure them and deploy the appplication.
### **The admin/management server should be reachable with a public IP.**
Configure security group rules to allow inbound IPv4 adresses using HTTP, HTTPS and SSH/RDP.  
The admin server cannot be placed in a private subnet, since this does not allow public IP's to reach it.
### **The admin/management server should be only reachable from trusted locations (office/admin's home).**
Configure the previously mentioned security group rules to only allow from the two trusted locations, both for SSH and for HTTP/HTTPS. So while reachable with a public IP adress, it can only be the public IP adress of one of the two trusted locations.
### **The following IP ranges are used: 10.10.10.0/24 & 10.20.20.0/24.**
One of these ranges is used for the PC containing the webserver, the other for the VPC containing the admin server.
### **All subnets need to be protected by a firewall at subnet level.**
Configure an Network ACL, possibly with a different set of rules for each of the subnets. The subnet which holds the admin server should only allow traffic from the trusted locations. The subnet which holds the web server can be accessed with all public IP's as it is publicly available, but SSH and RDP can only come from admin server.
### **SSH or RDP connections to the server are only allowed from the admin server.**
Configure a NACL and a security group for the web server to only allow SSH and RDP traffic from the admin server.
### **Allow improvements to the architecture, but be decisive in order to make the deadline.**
The placement of the admin server in a different region to the web server is a design flaw and can be improved upon byu placing the admin server in the same region but in a different AZ. In doing so, you will not need to use a VPC peering connection, thereby reducing latency and costs. 