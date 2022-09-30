# Processes

## Key terminology
- Processes  
The tasks that a computer performs.
- Daemon  
A program which runs in the background and is not interactive. They continue to exist and run regardles of any user being logged into the server if the computer is on.
- Services  
A proces that responds to requests of programs.
- Programs  
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
- Found out how much memory telnetd is using.
- Killed the telnetd process.