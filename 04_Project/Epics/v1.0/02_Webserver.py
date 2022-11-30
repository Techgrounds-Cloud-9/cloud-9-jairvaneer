# This IaC stack creates the webserver with all the requirements
# Public subnet with internet connection via HTTP/HTTPS, all IP's allowed open port 80
# Also SSH/RDP connection is only allowed from admin server open port 22 admin server
# Firewall protected at the subnet level
# So it requires both a security group and a Network ACL
# Deployment of webserver should be automated by use of user data

