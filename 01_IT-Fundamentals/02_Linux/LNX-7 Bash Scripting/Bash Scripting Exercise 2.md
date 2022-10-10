# Bash Scripting Exercise 2 & 3

## Key terminology
- Variables
- Conditions
- Bash Script  
See Assignment 7, Exercise 1.

## Exercise
### Sources
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
The script with conditions was not working for the first few times. I figured out this was because of the use of `#!/usr/bin/bash` while I should have been using `#!/bin/bash`.

### Results  
- Created a script that generated a random number between 1-10, stored it in a variable and appended that number to a text file. ![script random number](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%202%20-%20%231_Random_Number_Script.png) ![random number script output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%202%20-%20%232_Random_Number_Textfile.png)
- Created a script that generated a random number between 1-10, stored it in a variable, and appended that number to a text file if it was bigger than 5. If it was 5 or smaller, the line 'It's a small number buddy' was appended to the same text file instead. ![conditional number script](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%203%20-%20%231_Random_Number_Bigger_Than.png) 
- Used two seperate commands, `n=0; while [[ $n -lt 10 ]]; do ./randomif.sh; n=$((n+1)); done` and `for run in {1..10}; do ./randomif.sh; done` to run the script 10 times in a row, rather than inputting the command `./randomif.sh` to run it once multiple times to check whether the script worked. ![conditional number output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%203%20-%20%232_Random_Number_Line.png) ![conditional number output 2](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/651463abf8cd8f2922aaae47f99c6185784b3c61/00_includes/Sprint%201/Screenshots%20Linux/LNX-07%20Bash%20Scripting/LNX-07%20Exercise%203%20-%20%233_Random_Number_Line.png)