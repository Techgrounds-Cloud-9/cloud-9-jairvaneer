questions about architecture with product owner
scalability? not per se
static or dynamic IP? -> elastic IP
what are the IP's of the office and admin home -> we can make our own based on group


connection to the webserver are to be made from the admin server
v1.0 no elb or autoscaling, v1.1 yes

tomorrow at 2-3


aws_ec2.NetworkAcl
ec2.SecurityGroup


vpc->sg->nacl
webserver -> needs user script -> linux
adminserver: SG port 80 and 443 for own IP adresses, port 22 for SSH/RDP, only a portal no user data needed -> windows
scriptstorage ->
encryption ->
backup ->

both servers display index.html
bootstrap scripts in S3
server encryption

s3 bucket did not get destroyed
look out for resources not being destroyed