# Firewalls
A Firewall is software that filters internet traffic. In doing so, they provide a measure of security for clients.

## Key terminology
- **Firewalls**  
A firewall is a network security device that monitors incoming and outgoing network traffic and permits or blocks data packets based on a set of security rules. Its purpose is to establish a barrier between your internal network and incoming traffic from external sources (such as the internet) in order to block malicious traffic like viruses and hackers.
- **Statefull**  
A stateful firewall is a firewall that monitors the full state of active network connections. This means that stateful firewalls are constantly analyzing the complete context of traffic and data packets, seeking entry to a network rather than discrete traffic and data packets in isolation.
- **Stateless**  
Stateless firewalls are designed to protect networks based on static information such as source and destination. Stateless firewalls use packet filtering rules that specify certain match conditions. If match conditions are met, stateless firewall filters will then use a set of preapproved actions to guide packets into the network. If match conditions are not met, unidentified or malicious packets will be blocked.
## Exercise
### Sources
- https://www.makeuseof.com/tag/set-apache-web-server-3-easy-steps/  
- https://tipsntricks.in/how-to-fix-apache2-welcome-page-not-showing-in-ubuntu/  
- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04  
- https://www.layerstack.com/resources/tutorials/Installing-Apache-server-on-Linux-Cloud-Servers
- https://www.cyberciti.biz/faq/star-stop-restart-apache2-webserver/
- https://www.forcepoint.com/cyber-edu/firewall
- https://www.n-able.com/blog/stateful-vs-stateless-firewall-differences#:~:text=A%20stateful%20firewall%20is%20a,and%20data%20packets%20in%20isolation.
- 
### Overcome challenges
I used the wrong port to access the default landing page in my browser. Took me quite long to figure that out, team pointed me in the right direction.

### Results
- After installing Apache I was able to browse to the standard landing page for the apache webserver.  
![APache landing page](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/0ce94ceab78e4a3ea5f56efd78c1ec14c4b32318/00_includes/Sprint%202/Screenshots%20Security/SEC-02%20Firewalls/SEC-02%20Exercise%201%20-%20%231_Apache_Page.png)  
- By using the command `sudo ufw deny '80'` is was able to block internet traffic, while ssh was still open.  
![block traffic](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/0ce94ceab78e4a3ea5f56efd78c1ec14c4b32318/00_includes/Sprint%202/Screenshots%20Security/SEC-02%20Firewalls/SEC-02%20Exercise%201%20-%20%232_Firewall_Allow_SSH.png)