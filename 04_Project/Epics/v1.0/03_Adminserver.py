# This IaC stack creates an admin server with all the requirements
# Automated deployment by use of user data
# Placed in a public subnet
# Incoming: IP ranges used to access: 10.10.10.0/24 & 10.20.20.0/24 
# Outgoing: SSH/RDP (port 22) and HTTP/HTTPS (80/443)
# Configure security group and Network ACL