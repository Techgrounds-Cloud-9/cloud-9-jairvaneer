# IP Addresses
An Internet Protocol address is a numerical label that is connected to any network device that is connected to the internet.
## Key terminology
- **IP Adress**  
An IP adress is an unique address that is assigned to any network device. These addresses are then used by network devices to locate one another on a network.
- **IPv4**  
A common format for an IP address, made up of 32 bits/4 bytes, which are written in decimals. So four blocks of decimals, interspaced by a end-of-line point, where every block represents 1 byte. An example would be: 192.168.178.1   
- **NAT-Table**
Short for Network Address Translation Table. It is the heart of the NAT operation that takes place within the router, and makes it so that multiple devices on an internal network can function seperately on the same IP-adress and connect to the internet, without mixing up their connections and data.
- **IPv6**  
A newer version of INternet Protocol. Unlike the IPv4, which uses a 32-bit adress scheme written in decimals, Ipv6 uses a 128-bit address scheme which is written in hexadecimals, allowing for far more internet connections. 
- **ISP**  
Short for Internet Service Provider. This is a company that offers access to the internet for clients. Ziggo is an example of an ISP.  
- **Public IP**  
  A public IP address is an IP address that can be accessed directly over the internet and is assigned to your network router by your internet service provider (ISP). This is also called an external IP address.
- **Private IP**  
A private IP address is the address your network router assigns to your device. Each device within the same network is assigned a unique private IP address. This is how devices on the same internal network talk to each other.  
Private IP addresses let devices connected to the same network communicate with one another without connecting to the entire internet. By making it more difficult for an external host or user to establish a connection, private IPs help increase security within a specific network
- **Static IP Adress**  
A static IP address is an IP adress that is designated to the network or network device by the ISP. These don't change over time. This can be useful when hosting a website, or run a print service, or anything where other devices need to connect to a device. If the IP address is not static, but instead dynamic, the router settings on how to connect to that device would need to be updated every time the IP address changes.
- **Dynamic IP Adress**  
A dynamic IP adress is a temporary adress for devices connected to a network that continuously changes over time. This change can occur anytime from a few days to a few months. The IP addresses are configured by the DHCP  
- **DHCP**  
Short for Dynamic Host Configuration Protocol.
It is a network protocol or server that automatically configures IP addresses for any device on the network.

## Exercise
### Sources
- https://www.firewall.cx/networking-topics/network-address-translation-nat/228-nat-table.html
- https://community.fs.com/blog/ipv4-vs-ipv6-whats-the-difference.  
- https://www.okta.com/identity-101/internal-ip/#:~:text=Generally%2C%20your%20internal%20IP%20address,internet%20service%20provider%20(ISP)  
- https://www.internetvergelijk.nl/blog/wat-is-een-isp/  
- https://www.mysmartprice.com/gear/ip-address-how-to-find/#:~:text=Go%20to%20Settings%20and%20head,Android%20smartphone%20under%20Network%20details  
- https://www.geeksforgeeks.org/difference-between-static-and-dynamic-ip-address/
- https://www.techtarget.com/whatis/definition/dynamic-IP-address  
- https://www.lifewire.com/what-is-a-static-ip-address-2626012  
- https://nordvpn.com/nl/blog/wat-is-dhcp/  
- https://www.avast.com/c-ip-address-public-vs-private#:~:text=A%20public%20IP%20address%20is,through%20your%20router's%20public%20IP

### Overcome challenges
My public IP address for phone and laptop were not showing as the same. This took me quite some time to figure out, until I found that since iphone updated to IOS 15, they've provided and option named iCloud Private Relay, which masks your IP address. Turning that off provided the same public IP address for phone and laptop.

### Results
- Public IP address laptop and phone on wifi:  
Laptop: 178.85.64.168  
![IP laptop](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-05/NTW-05%20Exercise%201%20-%20%231_Public_IP_Laptop.png)  
Phone: 178.85.64.168  
![IP phone](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-05/NTW-05%20Exercise%201%20-%20%232_Public_IP_Phone.PNG)  

- The addresses are the same because we are using the same router to connect to the internet. This is the IP address that the router uses.
However, when using iCloud Private Relay, the public IP address of my phone is shown as 104.28.30.74  
![iCloud pivate relay](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-05/NTW-05%20Exercise%201%20-%20%233_Public_IP_Phone_ICloud_Private_Relay.PNG)
- Private IP address laptop and phone on wifi:  
Laptop: 192.168.178.115  
![Private IP Laptop](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-05/NTW-05%20Exercise%201%20-%20%234_Private_IP_Laptop.png)  
Phone: 192.168.178.157  
![Private IP phone](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-05/NTW-05%20Exercise%201%20-%20%235_Private_IP_Phone.PNG)  
- The addresses are not the same because the router assigns different internal IP adressess to all devices on a network. The router, however, has a seperate external IP address that is decided by the ISP.
- When I changed the private IP address of the phone to the private IP address of the laptop, I lost internet connection. ![Changed IP laptop](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aa84f58660b0f5d9e2154beefde64313c435cdbc/00_includes/Sprint%202/Screenshots%20Network/NTW-05/NTW-05%20Exercise%201%20-%20%236_Changed_IP_Phone_Laptop.PNG)
- When I changed the IP adress of my phone to an IP address outside my network I lost the connection to the internet.