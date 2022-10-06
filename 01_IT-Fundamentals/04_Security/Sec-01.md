# Network Detection
How to analyse a network. 
## Key terminology
- **Network**
- **Nmap**
- **Wireshark**  
See NTW-03.

## Exercise
### Sources


### Overcome challenges
When using the command `nmap 10.155.158.197` it returned `Host seems down`. By using the command `nmap -Pn 10.155.158.197` it showed that 1 host was running on the IP address. 

### Results
Scanned the Linux Machine using Nmap. Retrieved the IP address with the command `hostname -I`. The command `nmap localhost` showed that out of a 1000 ports, only two were open. Port 22 was used by SSH and port 80 by HTTP. {insert picture here}  Found out my IP address in the terminal. {insert picture here}  
Showed the connection being made on Wireshark. {insert picture here}