# Setting Up
This assignment deals with operating systems, in particular Linux, and how to set up a virtual machine.
## Key terminology
- **Hardware**  
The physical device that is being used to run software on, such as a laptop or desktop 

- **Software**  
All computer programs that can be used on different types of hardware are called software. 

- **OS**  
Short for Operating System. This manages the communication between the hardware and the software. It can be seen as a platform for the software to run on.  

- **Linux**  
An OS, such as Windows or MacOS. Unlike those, Linux is open-source, meaning that everyone can create new versions of it, and it is customizable and lightweight. 

- **Ubuntu**  
A version of the OS Linux. It is the version that we currently use. 

- **GUI**  
Short for Graphical User Interface. A GUI is a system of interactive visual components that convey information to the user. It is what most people see when they turn on the computer, and is one of two main ways to control a computer, the other being through the CLI. 

- **CLI**  
Short for Command-Line Interface. A CLI is a text-based user interface which can be used to run programs, manage files and interact with the computer, just like a GUI. Unlike the GUI, all browsing of the computer and its files are done from the command terminal, where commands are entered by the keyboard, after which the computer runs the command prompts.  

- **Terminal**  
A terminal is a window that is used to display a command line. In this window, commands are entered in order to navigate files on a computer or invoke actions.  

- **VM**  
Short for Virtual Machine. A VM is a resource that uses software instead of a physical device (hardware) to run programs or apps. It is used to run a seperate OS within the OS that is located on the physical "host”machine. Multiple VM's can run side-by-side, sep[erately, without interfering with each other. 

- **Hypervisor**  
Also known as a Virtual Machione Monitor or VMM, is software that creates and runs Virtual Machines (VMs). 

- **SSH**  
Short for Secure Shell, which is a protocol that allows to remotely connect to a machine. In this case we use the SSH to remotely connect to the Linux VM 

 

## Exercise
### Sources
- https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui  
- https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows  
- https://www.liquidweb.com/kb/putty-ssh-keys/  
- https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-convert-a-PEM-file-to-PPK
- https://www.computerhope.com/jargon/g/gui.htm  
- https://www.techtarget.com/searchwindowsserver/definition/command-line-interface-CLI  
- https://www.vmware.com/topics/glossary/content/hypervisor.html  
- https://www.vmware.com/topics/glossary/content/virtual-machine.html 

### Overcome challenges
Installing Powershell 5.1, didnt figure out how to get that working with the private key  
Switched to putty as openSSH client, struggled to open the PEM file with that until I figured out that I had to change the PEM file to the PPK file as that had the right permissions. Did that using PuttyGen, filled in the host-ip and ssh-port and it worked.  
Eventually and with the help of my team I was able to get Powershell working by inputting the following line of code:  
```ssh -i C:\Users\jairv\OneDrive\Bureaublad\Nest-Ja-Eer.pem jaïr_van@3.73.91.175 -p 52206```

### Results
- Made the connection by changing the format of the key file.
- Typing `whomami` showed my username.  