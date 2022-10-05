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
- **Class D and Class E IP Addresses**  
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
### Overcome challenges


### Results
