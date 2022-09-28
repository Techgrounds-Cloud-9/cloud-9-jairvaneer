# Working With Text (CLI)

## Key terminology
- Stdin  
Short for Standard Input. It is an input stream where data is sent to and read by a program. Usually, the keyboard is used for this.  
- Stdout  
Short for Standard Output. It is the fiel descriptor where a process can write output. When using the terminal, the Stdout is what is read on the screen when a command is given.  
- Terminal  
See Assignment Linux 1  
- I/O Redirection  
Short for Input/Output Redirection. It refers to the ability of the OS to change the stdin or stdout when executing a command on the terminal.  In other words, instead of reading the output of a command (input) on the screen (stdout), we can redirect it to a file or directory. This is done by using the > symbol or >> symbols.  
- Pipe  
A method to make the output of one command the input of another command. It is a form of redirection. 

## Exercise
### Sources
- https://www.computerhope.com/jargon/s/stdin.htm  
- https://www.computerhope.com/jargon/s/stdout.htm#:~:text=Stdout%2C%20also%20known%20as%20standard,defaults%20to%20the%20user's%20screen  
- https://www.educative.io/answers/how-to-do-input-output-redirection-in-linux  
- https://www.geeksforgeeks.org/how-to-create-a-text-file-using-the-command-line-in-linux  
- https://www.tecmint.com/linux-file-operations-commands/  
- https://stackoverflow.com/questions/9074353/terminal-command-to-find-lines-containing-a-specific-word  
- https://linuxhint.com/sed-command-to-delete-a-line/  
- https://linuxhint.com/redirect-output-file-screen-linux/  
- https://www.baeldung.com/linux/delete-lines-containing-string-from-file 

### Overcome challenges
In the proces of trying to copy a line to a new file while simultaneously deleting that line from the old file, I tried using the command `grep -i techgrounds newfile.txt > techgrounds.txt | sed'/techgrounds/d' newfile.txt`  
However, part of the code was wrong, as the last hyphen in the `sed'/techgrounds/'d` needed to be placed before the `d` and not after.  
While at first look the line was copied to the new file techgrounds.txt, and deleted from the old file newfile.txt, when using the command cat newfile.txt, the line reappeared, even though it did not disappear from the techgrounds.txt file, leading to believe that the pipe I had created did not work correctly. I will have to look into this. 

### Results
