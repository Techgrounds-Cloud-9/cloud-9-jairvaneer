# Bash Scripting Exercise 1

## Key terminology
- Bash Shell
- Bash Script
- Permissions
- Directory 
- PATH Variable 
- HTTPD
- Variables 

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
### Overcome challenges
- Wrote script to install apache2 as httpd server, but the script didn’t run, got the error bad interpreter: no such file or directory.
Had the syntax `#!/usr/bin/bash` as first line to execute the bash script, my team pointed out I had to remove the `/usr` bit, it ran succesfully after that. 

### Results
- Created a directory called 'scripts'.
- Added the scripts directory to the PATH variable.
- Created a script that appends a line of text to a text file whenever it was executed.
- Created a script that installed the httpd package, activated httpd, enabled httpd and printed the status of httpd in the terminal.