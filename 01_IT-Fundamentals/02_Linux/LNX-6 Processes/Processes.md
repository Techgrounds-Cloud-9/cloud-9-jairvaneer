# Processes
This assignment pertains to the tasks that a computer can perform and how to make it perform those task.
## Key terminology
- **Processes**  
The tasks that a computer performs.
- **Daemon**  
A program which runs in the background and is not interactive. They continue to exist and run regardles of any user being logged into the server if the computer is on.
- **Services**  
A proces that responds to requests of programs.
- **Programs**  
A process that is run and used by users.

## Exercise
### Sources
- https://www.cyberciti.biz/faq/how-do-i-turn-on-telnet-service-on-for-a-linuxfreebsd-system/  
- https://www.howtoforge.com/how-to-install-and-use-telnet-on-ubuntu/ 
- https://www.digitalocean.com/community/tutorials/telnet-command-linux-unix 
- https://www.ibm.com/docs/en/aix/7.2?topic=t-telnetd-daemon 
- https://phoenixnap.com/kb/how-to-kill-a-process-in-linux
- https://help.interfaceware.com/v6/differences-between-processes-daemons-and-services
### Overcome challenges
- `sudo apt-get install telnet` did not work, so used `sudo apt-get install telnetd -y`, that resolved the problem and installed telnet.

### Results
- Started the telnet daemon.  
- Found the PID of the telnet Daemon.
- Found out how much memory telnetd is using. ![telnet pid memory](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/7d9ce46dacf2a94c111fd38ea4a872072625d7ab/00_includes/Sprint%201/Screenshots%20Linux/LNX-06%20Processes/LNX-06%20Exercise%201%20-%20%231_2_3_Telnet_PID_Memory.png)
- Killed the telnetd process. ![kill telnet](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/7d9ce46dacf2a94c111fd38ea4a872072625d7ab/00_includes/Sprint%201/Screenshots%20Linux/LNX-06%20Processes/LNX-6%20Exercise%201%20-%20%234_Kill_Telnet.png) ![telnet stopped](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/7d9ce46dacf2a94c111fd38ea4a872072625d7ab/00_includes/Sprint%201/Screenshots%20Linux/LNX-06%20Processes/LNX-6%20Exercise%201%20-%20%234_Show_Process_Stopped.png)