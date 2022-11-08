# Security Groups
A security group controls the traffic that is allowed to reach and leave the resources that it is associated with.
## Key terminology
- **Security Groups**  
A stateful virtual firewall than can be assigned to instances, which runs in the VPC. A stateful system sends a request to the server and expect a response, track information, and resend the request if no response is received.  
A security group controls all traffic. For instance, if you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.  
When you create a VPC, it comes with a default security group. You can create additional security groups for each VPC. You can associate a security group only with resources in the VPC for which it is created.  
For each security group, you add rules that control the traffic based on protocols and port numbers. There are separate sets of rules for inbound traffic and outbound traffic.  
Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.
- **NACL**  
Short for Network Access Control List. This is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.
By default, a NACL is configured to allow all traffic in and out of the network.


## Exercise
### Sources
- https://www.spiceworks.com/tech/cloud/articles/stateful-vs-stateless/#:~:text=A%20stateless%20system%20sends%20a,if%20no%20response%20is%20received  
- https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html  
- https://www.knowledgehut.com/tutorials/aws/aws-nacl

### Overcome challenges
No problems, just learning.

### Results
