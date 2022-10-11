# Protocols

## Key terminology
- **Network Protocol**
- **Wireshark**  
Wireshark is a network protocol analyzer, an application that captures packets from a network connection. By feeding all the data in the packets through a set of filters, to be decided by the user, Wireshark is able to obtain and then visualize the data that the user wishes to see. In this way you can visualize network streams.
- **Packet**
A unit of data in a typical Ethernet network.

## Exercise
### Sources
- https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/
- https://www.guru99.com/layers-of-osi-model.html
- https://www.imperva.com/learn/application-security/osi-model/
- https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/
- https://what-when-how.com/data-communications-and-networking/network-standards-data-communications-and-networking/
- https://afteracademy.com/blog/what-are-protocols-and-what-are-the-key-elements-of-protocols
- https://www.comptia.org/content/guides/what-is-a-network-protocol
- https://www.quora.com/How-do-you-write-your-own-protocol-that-sits-on-top-of-TCP-IP
- https://stackoverflow.com/questions/18249847/how-to-build-a-protocol-on-top-of-tcp
- https://www.rfc-editor.org/rfc/rfc821
- https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it
- https://ipwithease.com/what-is-tcp-fin-packet/#:~:text=TCP%20Connection%20termination%20is%20a,be%20transmitted%20from%20the%20sender
- https://www.guru99.com/tcp-3-way-handshake.html


### Overcome challenges


### Results
- Insert image OSI stack protocol here
- Protocols  
A number of organisations are involved with determining what prtocols we use. These organisations are: 
1. The Institute of Electrical and Electronics Engineers (IEEE) 
2. The Internet Engineering Task Force (IETF)
3. The International Organization for Standardization (ISO)
4. The International Telecommunications Union (ITU)
5. The World Wide Web Consortium (W3C)  
In order to introduce your own internet protocol, you need to write a draft and submit it to the IETF if you want other people to use it, and for it to become a standardized network protocol.   
If it is just for private use, you can pick a port, design the protocol and write the code which defines what commands can be sent and how the receiver reacts to different commands. This is the software, which you can then implement and use.
- Found a TCP three way handshake occurring in my data. A Three way handshake is a process in which a TCP/IP network is useed yo make a connection between the server and the client. It is a three step process in which first is asked for synchronization (SYN), followed by an acknowledgment (SYN, ACK), which is thereafter acknowledged by the first side (ACK)
This can be seen in the screenshot.
Insert image here.