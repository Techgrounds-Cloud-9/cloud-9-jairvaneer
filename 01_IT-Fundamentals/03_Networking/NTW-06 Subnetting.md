# Subnetting
A network inside a network created to work more efficiently.
## Key terminology
- **Subnet**  
A network that is created and exists inside a network. Through this process networks are made more efficient, as network traffic can travel a shorter distance to its destination, without passing through unneccessary routers. When a network receieves data packets from another network, its sorts and routes those packets by subnet so the packets take the fastest route to their destination.  
Subnets are implemented by borrowing bits from the host end of an IP address in order to divide the larger network into smaller subnetworks. This is accomplished with the use of a subnet mask. The new, modified IP address will have the same network and host components as before, but will now feature a subnet component as well. Therefore, the less bits an IP address reserves for a network, the more apt it is to serve subnets on bigger networks. This is because subnets are implemented on the host side of an IP address, so more network bits means less bits for the host to offer a subnet mask.  
There are five classes of subnets: Class A, Class B, Class C, Class D and Class E. Subnet classes are made unique by the number of bits their IP addresses have dedicated to a network and the number of bits dedicated to hosts.  They each have a default subnet mask. Classes can be identified by the number in the first octet of their address:  

  Class A: First Octet Value 0-126  
Class B: First Octet Value 128-191  
Class C: First Octet Value 192-233  
Class D: First Octet Value 224-239  
Class E: First Octet Value 240-255  
   
   27 is not accounted for because it denotes a loopback address.  

- **Class A IP Address**  
A Class A IP adress reserves 8 bits of a total of 32 for a network, and the remaining 24 are dedicated to its hosts. Because of this a great number of hosts can be fitted on this IP address and therefore Class A IP addresses are best used to serve incredibly large networks. The Class A IP addresses range from 0-126 and its subnet mask is 255.0.0.0.  
- **Class B IP Address**  
Class B IP addresses are best served for smaller networks since they reserve 16 bits of a total of 32 bits for the network, leaving  16 bits for the host.  Network addresses for these range from 128 to 191. Consequently, the default subnet mask for Class B is 255.255.0.0. My apartments'public IP address is 178.85.64.168, which tells me that it is a Class B IP address and is part of a smaller network, probably covering the neigbourhood or block. 
- **Class C IP Address**  
Class C IP addresses are normally assigned to a very small-sized network. They reserve 24 bits of a total of 32 bits for the network, leaving only 8 bits for the host. Their IP addresses range from 192 to 233 and their default subnet mask is 255.255.255.0. The private IP address of my laptop is 192.168.178.115, while the private IP address of my phone is 192.168.178.157.  This means that they are both on the same Class C subnet, .  
- **Class D & Class E IP Addresses**  
The uses of Class D and Class E IP addresses are mostly reserved for experimental purposes. For instance, a Class D IP address is almost exclusively reserved for multicasting applications. (Multicasting is a method of routing data on a computer network that allows a single or group of senders to communicate with a group of receivers). Unlike Classes A, B, and C, Class D is not available for use in normal networking operations. They don’t have subnet potential because there are no host bits within the Class D address space.  
Class E is often cited as having been created for future use, research, and development. Although these IP addresses are reserved, their actual use has never developed. As a result, most network implementations disregard this class altogether. In fact, Class E is sometimes classified as illegal or undefined.
- **Subnet Mask**  
A 32-bit number that tells the router which bit of the IP-address is for the network portion and which bit is for the host portion. It is a binary number, but usually formatted in dotted decimal or CIDR format for us to distinguish. A subnet mask that can be found is 255.255.0.0. This is the dotted decimal way of showing a subnet mask. The binary notation would look like 11111111.11111111.00000000.00000000. Thie CIDR notation uses the prefix "/" at the end of the IP address to denominate the subnet mask, so that would be /16.  
This subnet mask signals that the first two parts of the IPv4 address, which is made up of four parts, are to denominate the network, and the last two parts are to denominate the host. An IP address with a subnet mask as shown in the example would point to a host on a Class B subnetwork.  
For IPv6 the default subnet mask is /64, meaning that the first 64 bits are the network portion. You could subnet this to make a few smaller networks as with the default mask you have 18,446,744,073,709,551,616 possible addresses on one IPv6 network.
- **IP Address**  
See NTW_05.
- **LAN**  
See NTW_01.
- **Host**  
A host is a device that contains data or programs that other devices can access through a network or a modem.
- **CIDR notation**  
Short for Classless Inter-Domain Routing. It is an alternative manner of representing a subnet mask. It is simply a count of the number of network bits in a subnet mask and is usually preceded by a prefix "/". So my IP address 178.85.64.168, which has a subnet mask of 255.255.0.0 as it is on a Class B subnet, which makes use of 14 bits for the network portion of the IP adress, would be represented as 178.85.64.168/14.
## Exercise
### Sources
- https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/
- https://www.n-able.com/blog/overview-of-subnet-classes  
- https://avinetworks.com/glossary/subnet-mask/  
- https://www.controltechnology.com/Files/common-documents/application_notes/Understanding-CIDR-Notation-for-IP-Address-Display  
- https://www.sciencedirect.com/topics/computer-science/subnet-mask  
- https://www.finseth.com/parts/address.php  
- https://www.geeksforgeeks.org/how-to-calculate-number-of-host-in-a-subnet/#:~:text=In%20simple%20words%2C%20the%20Number,bits%20in%20the%20IP%20address  
- https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html
- https://www.linkedin.com/pulse/connecting-internet-from-ec2-instance-private-subnet-aws-thandra
- https://www.whizlabs.com/blog/aws-solutions-architect-associate-exam-questions/  
- https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway-c9177e710af6 


### Overcome challenges
I was looking into NAT GAteways for VPC, Virtual Private Cloud, where they have to be placed inside the Public Subnet instead of in the Private Subnet in order to connect the Private Subnet to the internet. SO for some time I wasw a bit confused on how to draw the diagram, until I realized I needed to look at a VN, a Virtual network, instead of a VPC. 

### Results
In order to create the network architecture that is asked, we need to create a VN, a Virtual Network with 3 subnets with a total of 51 hosts, so we use a Class C network, as this is capable of hosting 256 IP addresses. We dont use the first and last addresses in any class, so no 192.168.0.0 or 192.168.0.256. They are not used for any hosts because the first IP address is used to represent the whole network ID while the last IP address is used as the broadcast address. 

So, to calculate the possible number of hosts in a network we subtract 2. In the case of a Class C network with a maximum of 256 hosts, that gives 254.   
We will use the following IP address as a starting point: 192.168.0.1/24 with subnet mask 255.255.255.0   

To work as efficiently as possible, we want as little extra hosting space per subnet. To calculate what IP address to use, we divide the maximum number of hosts (256) by two, dividing that answer by two until we would hit a number lower than our number of hosts. For every time we divide by two we go up one number on the CIDR notation.  

((256/2)/2)/2=32.  

32/2=16, but we need to subtract another 2 for the first and last IP addresses that remain unused so that gives us 14. We need 15, so three divisions is enough. The starting CIDR number 24+3=27. An IP address with CIDR/27 gives us 30 host adresses. 

This means that for Private Subnet A 192.168.0.0/27 is the network ID, 192.168.0.1/27 - 192.168.0.30/27 are our usable IP adresses, 192.168.0.31/27 is our broadcast address and the subnet mask is 255.255.255.224. 

For Private Subnet B we need 31 hosts + the NAt Gateway, which makes 31 host IP adresses needed.

/27 only provided 32 IP adresses, so we need /26 which provides 64-2=62 IP adressess.  . This means that for Private Subnet B the network ID is 192.168.0.32/27, the usable IP addresses are 192.168.0.33/26 - 192.168.0.94/26 and the broadcast address is 192.168.0.95/26 and the subnet mask is 255.255.255.192. 

For Public Subnet C we need five hosts + Internet Gateway = six so /29. The network ID is 192.168.0.96/29, the IP addresses range from 198.168.0.97/29 - 198.168.0.102/29, the broadcast address is 192.168.0.103/29 and the subnet mask is 255.255.255.248.  
![Subnetting](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-06/NTW-06%20Exercise%201%20-%20%232_Virtual_Network.png)
![Available hosts](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-06/NTW-06%20Exercise%201%20-%231_Table_Available%20Host_Class_C_Network.png)