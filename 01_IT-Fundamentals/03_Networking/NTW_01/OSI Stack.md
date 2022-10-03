# OSI Stack

## Key terminology
- OSI Model  
Short for Open Systems Interconnection. It is a 7 layer architecture with each layer having a specific functionality to perform. All these 7 layers work together to transmit data from one person to the other.  
The 7 layers are divided in Media Layers (1-3) and Host Layers (4-7).   
***Media Layers:***  
**1. Physical Layer:** This layer is responsible for the actual physical connection between the devices. This layer contains data in bits. It is responsible for transmitting individual bits from one node to the next. When receiving data, this layer will get the signal received and convert it into 0s and 1s and send them to the Data Link layer, which will put the frame back together.  
At the physical layer, one might find “physical” resources such as network hubs, cabling, repeaters, network adapters or modems.  
The functions of the physical layer are:  
*1. Bit synchronization:* The physical layer provides the synchronization of the bits by providing a clock. This clock controls both sender and receiver thus providing synchronization at bit level.  
*2. Bit rate control:* The Physical layer also defines the transmission rate i.e. the number of bits sent per second.  
*3. Physical topologies:* Physical layer specifies the way in which the different, devices/nodes are arranged in a network i.e. bus, star, or mesh topology.  
*4. Transmission mode:* Physical layer also defines the way in which the data flows between the two connected devices. The various transmission modes possible are Simplex, half-duplex and full-duplex.  
**2. Data Link Layer (DLL):** The data link layer is responsible for the node-to-node delivery of the message. The main function of this layer is to make sure data transfer is error-free from one node to another, over the physical layer. When a packet arrives in a network, it is the responsibility of DLL to transmit it to the Host using its MAC address.  
Data Link Layer is divided into two sublayers, which will be discussed later: the *Logical Link Control (LLC)* & the *Media Access Control (MAC)*.  
 The packet received from the Network layer is further divided into frames depending on the frame size of NIC (Network Interface Card). DLL also encapsulates Sender and Receiver’s MAC address in the header.  
 The Receiver’s MAC address is obtained by placing an ARP (Address Resolution Protocol) request onto the wire asking “Who has that IP address?” and the destination host will reply with its MAC address.  
 The functions of the Data Link layer are :  
 *1. Framing:* Framing is a function of the data link layer. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver. This can be accomplished by attaching special bit patterns to the beginning and end of the frame.  
 *2. Physical addressing:* After creating frames, the Data link layer adds physical addresses (MAC address) of the sender and/or receiver in the header of each frame.  
 *3. Error control:* Data link layer provides the mechanism of error control in which it detects and retransmits damaged or lost frames.  
 *4. Flow Control:* The data rate must be constant on both sides else the data may get corrupted thus, flow control coordinates the amount of data that can be sent before receiving acknowledgement.  
 *5. Access control:* When a single communication channel is shared by multiple devices, the MAC sub-layer of the data link layer helps to determine which device has control over the channel at a given time.  
 **3. Network Layer:** The network layer works for the transmission of data from one host to the other located in different networks. It also takes care of packet routing i.e. selection of the shortest path to transmit the packet, from the number of routes available. The sender & receiver’s IP addresses are placed in the header by the network layer.  
 The functions of the Network layer are:  
 *1. Routing:* The network layer protocols determine which route is suitable from source to destination. This function of the network layer is known as routing.  
 *2. Logical Addressing:* In order to identify each device on internetwork uniquely, the network layer defines an addressing scheme. The sender & receiver’s IP addresses are placed in the header by the network layer. Such an address distinguishes each device uniquely and universally.  
 ***Host Layers:***  
 **4. Transport Layer:** Also referred to as the Heart of the OSI Model. The transport layer provides services to the application layer and takes services from the network layer. The data in the transport layer is referred to as *Segments*. It is responsible for the End to End Delivery of the complete message. The transport layer also provides the acknowledgement of the successful data transmission and re-transmits the data if an error is found.  
At sender’s side: Transport layer receives the formatted data from the upper layers, performs *Segmentation*, and also implements *Flow & Error control* to ensure proper data transmission. It also adds Source and Destination port numbers in its header and forwards the segmented data to the Network Layer. Generally, this destination port number is configured, either by default or manually. For example, when a web application makes a request to a web server, it typically uses port number 80, because this is the default port assigned to web applications. Many applications have default ports assigned.  
At receiver’s side: The Transport Layer reads the port number from its header and forwards the Data which it has received to the respective application. It also performs sequencing and reassembling of the segmented data.  
The functions of the transport layer are:  
*1. Segmentation and Reassembly:* This layer accepts the message from the (session) layer, and breaks the message into smaller units. Each of the segments produced has a header associated with it. The transport layer at the destination station reassembles the message.  
*2. Service Point Addressing:* In order to deliver the message to the correct process, the transport layer header includes a type of address called service point address or port address. Thus by specifying this address, the transport layer makes sure that the message is delivered to the correct process.  
The services provided by the transport layer:  
A. Connection-Oriented Service: It is a three-phase process that includes  
– Connection Establishment  
– Data Transfer  
– Termination / disconnection  
In this type of transmission, the receiving device sends an acknowledgement, back to the source after a packet or group of packets is received. This type of transmission is reliable and secure.  
B. Connectionless service: It is a one-phase process and includes Data Transfer. In this type of transmission, the receiver does not acknowledge receipt of a packet. This approach allows for much faster communication between devices. Connection-oriented service is more reliable than connectionless Service.  
**5. Session Layer:**  This layer is responsible for the establishment of connection, maintenance of sessions, authentication, and also ensures security. 
The functions of the session layer are:  
*1. Session establishment, maintenance, and termination:* The layer allows the two processes to establish, use and terminate a connection.  
*2. Synchronization:* This layer allows a process to add checkpoints which are considered synchronization points into the data. These synchronization points help to identify the error so that the data is re-synchronized properly, and ends of the messages are not cut prematurely and data loss is avoided.  
*3. Dialog Controller:* The session layer allows two systems to start communication with each other in half-duplex or full-duplex.  
**6. Presentation Layer:**  The presentation layer is also called the Translation layer. The data from the application layer is extracted here and manipulated as per the required format to transmit over the network.  
The functions of the presentation layer are: 
*1.Translation:* Translating different encryption systems to one another. For example, *ASCII (American Standard Code for Information Exchange)* to *EBCDIC (Extended Binary-Coded Decimal Interchange Code)*. These two different encryption systems are widely used and sometimes need to be translated in order for systems to decrypt them.
*2. Encryption/ Decryption:* Data encryption translates the data into another form or code. The encrypted data is known as the ciphertext and the decrypted data is known as plain text. A key value is used for encrypting as well as decrypting data.  
*3. Compression:* Reduces the number of bits that need to be transmitted on the network.  
**7. Application Layer:**  
The top layer of the OSI Reference Model stack of layers is the Application layer which is implemented by the network applications. These applications produce the data, which has to be transferred over the network. This layer also serves as a window for the application services to access the network and for displaying the received information to the user.  
The functions of the Application layer are:  
*1. Network Virtual Terminal*  
*2. FTAM-File transfer access and management*  
*3. Mail Services*  
*4. Directory Services*
- Bits  
A bit is a binary digit, the smallest increment of data on a computer. A bit can hold only one of two values: 0 or 1, corresponding to the electrical values of off or on, respectively. Bits are usually assembled into a group of eight to form a byte. A byte contains enough information to store a single ASCII character, like "h".
- Byte  
A Byte is a small piece of data, not to be confused with bits, an even smaller data increment. To denote the various sizes of memory and data storage the following units exist.  
*1 Byte*  
1 kilobyte  (KB) = 1024 bytes  
1 megabyte  (MB) = 1024 KB  
1 gigabyte  (GB) = 1024 MB  
1 terabyte  (TB) = 1024 GB  
1 petabyte  (PB) = 1024 TB  
1 exabyte   (EB) = 1024 PB  
1 zettabyte (ZB) = 1024 EB  
1 yottabyte (YB) = 1024 ZB
- LLC  
Short for Logical Link Control. It is a sublayer of the Data Link Layer which provides the logic as it controls the synchronization, multiplexing, flow control and error-checking functions.
- MAC  
Short for Media Access Control. A MAC adress is the identification number for the hardware. The NIC of every piece of hardware has a unchangeable MAC adress that is embedded by the vendor at the time of manufacturing. It is an unique ID used to identify specific network interface cards. 
- NIC  
Short for Network Interface Card. It is a hardware component without which a computer cannot be connected over a network. It is a circuit board installed in a computer that provides a dedicated network connection to the computer. It is also called a *network interface controller*, *network adapter* or *LAN adapter*.
- LAN  
Short for Local Area Network. It is  collection of devices connected together within one physical location. These can be small, such as an house, or big, like an office or a school. However the size, the defining characteristic of a LAN is that the connected devices are in a limited area. 
- WAN  
Short for Wide Area Network. It does the same as a LAN, but for a larger geographical area. Some WANs connect many LANs together.
- MAN  
Short for Metropolitan Area Network. It does the same as a LAN, but for a larger geographical area. Some MANs connect many LANs together.
- ARP  
Short for Address Resolution Protocol. It is a procedure that connects an ever-changing Internet Protocol (IP) address to a fixed machine adress, also known as a media access control (MAC) adress, in a local area network (LAN). This mapping procedure is important because the lengths of the IP and MAC addresses differ, and a translation is needed so that the systems can recognize one another. The most used IP today is IP version 4 (IPv4). An IP address is 32 bits long. However, MAC addresses are 48 bits long. ARP translates the 32-bit address to 48 and vice versa.
- IP  
Short for Internet Protocol. An IP address is a unique address that identifies a device on the internet or a local network. The Internet Protocol is the set of rules governing the format of data sent via the internet or local network.  
In essence, IP addresses are the identifier that allows information to be sent between devices on a network: they contain location information and make devices accessible for communication. The internet needs a way to differentiate between different computers, routers, and websites. IP addresses provide a way of doing so.
- Segments & Segmentation  
Packet segmentation is the process of dividing a data packet into smaller units (segments) for transmission over the network. Packet segmentation happens at layer four of the OSI model; the Transport Layer. Segmentation may be required when the data packet is larger than the maximum transmission unit supported by the network, or when the network is unreliable and it is desirable to divide the information into smaller segments to maximize the probability that each one of them can be delivered correctly to the destination.
- Flow Control 
An important function of the Data Link Layer. It refers to a set of procedures that tells the sender how much data it can transmit before waiting or acknowledgement from the receiver.
- Error Control  
The error control function of the Data Link Layer detects the errors in transmitted frames and re-transmits all the erroneous frames. It helps in dealing with data frames that are damaged in transit, data frames lost in transit, and the acknowledgement frames that are lost in transmission. The method used for error control is called Automatic Repeat Request which is used for the noisy channel. 
- Ports  
A port is a virtual point where network connections start and end.  Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection.  
Ports are standardized across all network-connected devices, with each port assigned a number. Most ports are reserved for certain protocols — for example, all Hypertext Transfer Protocol (HTTP) messages go to port 80. While IP addresses enable messages to go to and from specific devices, port numbers allow targeting of specific services or applications within those devices.
- Troubleshooting  
Troubleshooting is a systematic approach to problem-solving that is often used to find and correct issues with complex machines, electronics, computers and software systems.
- TCP/IP Model  
Short for Transmission Control Protocol/Internet Protocol. It is a concise version of the OSI model and contains four layers. These layers are:  
**1. Network Access Layer:**  This layer corresponds to the combination of the Data Link Layer and the Physical Layer of the OSI model. It looks out for hardware adressing and the protocols present in this layer allows for the physical transmission of data.
**2. Internet Layer:**  
This layer parallels the functions of OSI’s Network layer. It defines the protocols which are responsible for logical transmission of data over the entire network. The main protocols residing at this layer are:  
*IP:* Short for Internet Protocol. It is responsible for delivering packets from the source host to the destination host by looking at the IP addresses in the packet headers. IP has 2 versions: *IPv4* and *IPv6*. IPv4 is the one that most of the websites are using currently. But IPv6 is growing as the number of IPv4 addresses are limited in number when compared to the number of users.  
*2. ICMP:* Short for Internet Control Message Protocol. It is encapsulated within IP datagrams and is responsible for providing hosts with information about network problems.
*3. ARP:* Short for Address Resolution Protocol. Its job is to find the hardware address of a host from a known IP address. ARP has several types: Reverse ARP, Proxy ARP, Gratuitous ARP and Inverse ARP.  
**3. Host-to-Host Layer:**  This layer is analogous to the transport layer of the OSI model. It is responsible for end-to-end communication and error-free delivery of data. It shields the upper-layer applications from the complexities of data. The two main protocols present in this layer are:  
*1. Transmission Control Protocol (TCP):* It is known to provide reliable and error-free communication between end systems. It performs sequencing and segmentation of data. It also has acknowledgment feature and controls the flow of the data through flow control mechanism. It is a very effective protocol but has a lot of overhead due to such features. Increased overhead leads to increased cost.  
*2. User Datagram Protocol (UDP):* It is the go-to protocol if your application does not require reliable transport as it is very cost-effective. Unlike TCP, which is connection-oriented protocol, UDP is connectionless.  
**4. Process/Application Layer:** This layer performs the functions of top three layers of the OSI model: Application, Presentation and Session Layer. It is responsible for node-to-node communication and controls user-interface specifications. Some of the protocols present in this layer are:  
*1: HTTP and HTTPS:* HTTP stands for Hypertext transfer protocol. It is used by the World Wide Web to manage communications between web browsers and servers. HTTPS stands for HTTP-Secure. It is a combination of HTTP with SSL (Secure Socket Layer). It is efficient in cases where the browser need to fill out forms, sign in, authenticate and carry out bank transactions.  
*2: SSH:* SSH stands for Secure Shell. It is a terminal emulations software similar to Telnet. The reason SSH is more preferred is because of its ability to maintain the encrypted connection. It sets up a secure session over a TCP/IP connection.  
*3: NTP:* NTP stands for Network Time Protocol. It is used to synchronize the clocks on computers to one standard time source. It is very useful in a number of situiations, as a server can crash very badly if it’s out of sync.

## Exercise
### Sources  
- https://www.forcepoint.com/cyber-edu/osi-model
- https://www.securitysales.com/columns/7-layers-network-communications/#:~:text=Layers%20one%20through%20three%20are,software%20that%20implements%20network%20services.
- https://www.geeksforgeeks.org/layers-of-osi-model/  
- https://www.guru99.com/difference-tcp-ip-vs-osi-model.html  
- https://www.imperva.com/learn/application-security/osi-model/  
- https://www.qquest.nl/beheer/osi-model/
- https://www.ascii-code.com/
- https://www.techtarget.com/whatis/definition/EBCDIC-Extended-Binary-Coded-Decimal-Interchange-Code
- https://kb.iu.edu/d/ackw
- https://www.geeksforgeeks.org/logical-link-control-llc-protocol-data-unit/  
- https://www.geeksforgeeks.org/mac-full-form/  
- https://www.tutorialspoint.com/what-is-network-interface-card-nic  
- https://www.cisco.com/c/en/us/products/switches/what-is-a-lan-local-area-network.html
- https://www.fortinet.com/resources/cyberglossary/what-is-arp
- https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address  
- http://www.cnt4all.com/2016/08/07-transport-layer-segmentation.html#:~:text=Segmentation%20means%20to%20divide%20something,layer%20is%20segment(s).
- https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/  
- https://www.spiceworks.com/it-articles/troubleshooting-steps/  
- https://www.geeksforgeeks.org/tcp-ip-model/  



### Overcome challenges
The understanding of two different models, which were entirely foreign to me, and the numerous terms and concepts involved with the models, proved some difficulty in unerstanding. With the help of numerous articles I was able to graps the concepts and models from this assignment.

### Results
Understand the difference between the OSI and the TCP/IP models, the terminology included in either, and when to use the one versus the other.