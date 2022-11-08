# Bash Scripting Exercise 1

## Key terminology
- **Bash**  
Short for Bourne Again Shell.  A shell is a command interpreter, software that figures out what the different command inputs in the CLI mean.
- **Bash Script**  
A Bash script is a plain text file which contains a series of commands.
- **Permissions**  
In Linux, file permissions, attributes, and ownership control the access level that the system processes and users have to files. This ensures that only authorized users and processes can access specific files and directories.
- **Directory**  
 A directory is a unique type of file that contains only the information needed to access files or other directories. As a result, a directory occupies less space than other types of files. File systems consist of groups of directories and the files within the directories.
- **PATH Variable**  
 The PATH environment variable is an important security control. It specifies the directories to be searched to find a command. The default systemwide PATH value is specified in the `/etc/profile` file, and each user normally has a PATH value in the user's `$HOME/`.
- **HTTPD**  
HTTPd is a software program, that usually runs in the background, as a process. It plays the role of server in a client-server model using HTTP and/or HTTPS network protocols. HTTPd waits for the incoming client requests and for each request it answers by replying with requested information.
- **Variables**  
Variables are areas of memory that can be used to store information and are referred to by a name. Whenever the shell sees a word that begins with a "$", it tries to find out what was assigned to the variable and substitutes it.To create a variable, put a line in the script that contains the name of the variable followed immediately by an equal sign ("="). No spaces are allowed. After the equal sign, assign the information to store.
- **Conditions**  
Conditions can be used within a script or automation to prevent further execution. When a condition does not return true, the script or automation stops. A condition will look at the system at that moment. For example, a condition can test if a switch is currently turned on or off.
Unlike a trigger, which is always `or`, conditions are `and` by default, since all conditions have to be true.

## Exercise
### Sources
- https://linuxize.com/post/how-to-add-directory-to-path-in-linux/ 
- https://linuxize.com/post/bash-append-to-file/ 
- https://linuxhint.com/bash_append_line_to_file/ 
- https://www.freecodecamp.org/news/shell-scripting-crash-course-how-to-write-bash-scripts-in-linux/ 
- https://www.andrewcbancroft.com/blog/musings/make-bash-script-executable/ 
- https://www.taniarascia.com/how-to-create-and-use-bash-scripts/ 
- https://www.layerstack.com/resources/tutorials/Installing-Apache-server-on-Linux-Cloud-Servers
- https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04-quickstart 
https://medium.com/@ertorrez/use-a-script-to-install-and-launch-an-apache-server-on-centos-8-6db6e4b81cbf  
- https://stackoverflow.com/questions/8988824/generating-random-number-between-1-and-10-in-bash-shell-script 
- https://acloudguru.com/blog/engineering/conditions-in-bash-scripting-if-statements 
- https://unix.stackexchange.com/questions/119546/starting-with-bash-lt-and-gt-arguments 
- https://blog.eduonix.com/shell-scripting/generating-random-numbers-in-linux-shell-scripting/ 
- https://linuxhint.com/generate-random-number-bash/ 
- https://stackoverflow.com/questions/1194882/how-to-generate-random-number-in-bash 
- https://tldp.org/LDP/abs/html/randomvar.html 
- https://stackoverflow.com/questions/3737740/is-there-a-better-way-to-run-a-command-n-times-in-bash
- https://linuxize.com/post/bash-if-else-statement/  
- https://www.ibm.com/docs/ssw_aix_72/devicemanagement/directories.htm  
- https://acloudguru.com/blog/engineering/conditions-in-bash-scripting-if-statements
### Overcome challenges
- Wrote script to install apache2 as httpd server, but the script didn’t run, got the error bad interpreter: no such file or directory.
 The scripts were not not working for the first few times. I figured out this was because of the use of `#!/usr/bin/bash` while I should have been using `#!/bin/bash` to get the script to execute.

### Results
- Created a directory called 'scripts'.
- Added the scripts directory to the PATH variable. ![scripts added path](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%201%20-%20%231_Scripts_Directory_Path_Variable.png)
- Created a script that appends a line of text to a text file whenever it was executed. ![append line script](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%201%20-%20%232_Script_Appends_Line.png)
- Created a script that installed the httpd package, activated httpd, enabled httpd and printed the status of httpd in the terminal. ![httpd script](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%201%20-%20%233_HTTPD_Script.png) ![httpd script output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%201%20-%20%234_Run%20HTTPD_Script.png) ![httpd script output 2](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%201%20-%20%235_Run%20HTTPD_Script.png)  
- Created a script that generated a random number between 1-10, stored it in a variable and appended that number to a text file. ![script random number](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%202%20-%20%231_Random_Number_Script.png) ![random number script output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%202%20-%20%232_Random_Number_Textfile.png)
- Created a script that generated a random number between 1-10, stored it in a variable, and appended that number to a text file if it was bigger than 5. If it was 5 or smaller, the line 'It's a small number buddy' was appended to the same text file instead. ![conditional number script](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%203%20-%20%231_Random_Number_Bigger_Than.png) 
- Used two seperate commands, `n=0; while [[ $n -lt 10 ]]; do ./randomif.sh; n=$((n+1)); done` and `for run in {1..10}; do ./randomif.sh; done` to run the script 10 times in a row, rather than inputting the command `./randomif.sh` to run it once multiple times to check whether the script worked. ![conditional number output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%203%20-%20%232_Random_Number_Line.png) ![conditional number output 2](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%203%20-%20%233_Random_Number_Line.png)