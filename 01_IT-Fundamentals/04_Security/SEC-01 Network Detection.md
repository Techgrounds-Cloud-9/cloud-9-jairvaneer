# Network Detection
How to analyse a network. 
## Key terminology
- **Network**  
See NTW-02.
- **Nmap**  
Nmap ("Network Mapper") is a free and open source utility for network discovery and security auditing. Nmap uses raw IP packets to determine what hosts are available on the network, what services those hosts are offering, what operating systems they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. It was designed to rapidly scan large networks, but works fine against single hosts.
- **Wireshark**  
See NTW-03.

## Exercise
### Sources
- https://www.ionos.com/digitalguide/server/know-how/what-is-a-network/#:~:text=In%20information%20technology%2C%20a%20network,peer%2Dto%2Dpeer%20network  
- https://nmap.org/ 
- https://phoenixnap.com/kb/nmap-commands

### Overcome challenges
When using the command `nmap 10.155.158.197` it returned `Host seems down`. By using the command `nmap -Pn 10.155.158.197` it showed that 1 host was running on the IP address. 

### Results
- Scanned the Linux Machine using Nmap. Retrieved the IP address with the command `hostname -I`. The command `nmap localhost` showed that out of a 1000 ports, only two were open. Port 22 was used by SSH and port 80 by HTTP.   
![Nmap](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/ce19f1fcf00f621cb21a3e563a3fa078bbac345d/00_includes/Sprint%202/Screenshots%20Security/SEC-01%20Network%20Detection/Sec-01%20Exercise%201%20-%20%231_Nmap.png)  
- Found out my IP address in the terminal.  
![source IP](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/ce19f1fcf00f621cb21a3e563a3fa078bbac345d/00_includes/Sprint%202/Screenshots%20Security/SEC-01%20Network%20Detection/Sec-01%20Exercise%201%20-%20%232_Confirm_Source_IP.png)  
- Showed the connection being made on Wireshark.  
![wireshark](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/ce19f1fcf00f621cb21a3e563a3fa078bbac345d/00_includes/Sprint%202/Screenshots%20Security/SEC-01%20Network%20Detection/Sec-01%20Exercise%201%20-%20%232_Wireshark.png)