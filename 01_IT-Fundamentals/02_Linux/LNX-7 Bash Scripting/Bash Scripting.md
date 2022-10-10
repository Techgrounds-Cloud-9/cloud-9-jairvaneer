# Bash Scripting Exercise 1

## Key terminology
- Bash Shell
- Bash Script
- Permissions
- Directory 
- PATH Variable 
- HTTPD
- Variables  
- Conditions 

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