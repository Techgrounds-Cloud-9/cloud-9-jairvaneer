# Files and Directories
This assignment pertains to the ways in wich data is structured on a computer. 
## Key terminology
- **Directory**  
A directory is a file cataloging structure used on computers. Directories are also known as folders, which can contain files. It is often pictured as a tree, with the root directory at its base, and all other directories branching out from there. 

- **Folder**  
A folder holds one or more files but can also contain one or more folders. It is sometimes also called a directory. It provides a way to organize files on a computer. 

- **File**  
The common storage unit in a computer. All programs and data are written into files of their own and read from that file. 

- **Terminal**  
See LNX-01 

## Exercise
### Sources
- https://www.hostinger.com/tutorials/linux-commands  
- https://help.ubuntu.com/community/UsingTheTerminal  
- https://www.geeksforgeeks.org/how-to-create-a-text-file-using-the-command-line-in-linux/  
- https://www.educative.io/answers/how-to-resolve-the-permission-denied-error-in-linux  
- https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/#:~:text=An%20absolute%20path%20is%20defined%20as%20specifying%20the%20location%20of,actual%20file%20system%20from%20%2F%20directory.&text=Relative%20path%20is%20defined%20as,present%20working%20directly(pwd)  
- https://www.pcmag.com/encyclopedia/term/files-vs-folders 

 

### Overcome challenges

Finding the working directory was quite easy, using the ```pwd``` command. However it turned out that the assignment asked us to look for directories that didnt exist. After we realized this, we found what we had to look for and creating a directory went easy enough. After this I did not have permission to create a new file but by using the command ```sudo chmod 777 techgrounds```, I was able to to create a text file in the techgrounds directory that we created earlier. 
### Results
- Found the working directory.  
![pwd](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4dcf369698c33089e31155764ec6b3c1263e94f2/00_includes/Sprint%201/Screenshots%20Linux/LNX-02%20Files%20and%20Directories/LNX-02%20Exercise%201%20-%20%231_Current_Working_Directory.png)
- Made a listing of all files and directories in home directory.  
![ls](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4dcf369698c33089e31155764ec6b3c1263e94f2/00_includes/Sprint%201/Screenshots%20Linux/LNX-02%20Files%20and%20Directories/LNX-02%20Exercise%201%20-%20%232_Directories.png)
- Created a new directory called techgrounds.  
![mkdir techgrounds](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4dcf369698c33089e31155764ec6b3c1263e94f2/00_includes/Sprint%201/Screenshots%20Linux/LNX-02%20Files%20and%20Directories/LNX-02%20Exercise%201%20-%20%233_Create_New_Directory_Techgrounds.png)
- Created a text file in the new directory I created.  
![cat newfile](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4dcf369698c33089e31155764ec6b3c1263e94f2/00_includes/Sprint%201/Screenshots%20Linux/LNX-02%20Files%20and%20Directories/LNX-02%20Exercise%201%20-%20%234_Create_New_File.png)
- Moved around the directory tree using both absolute and relative paths by using command `cd <directory>` for an absolute path and the command `cd ..` for a relative path.  
![absolute relative moving](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/4dcf369698c33089e31155764ec6b3c1263e94f2/00_includes/Sprint%201/Screenshots%20Linux/LNX-02%20Files%20and%20Directories/LNX-02%20Exercise%201%20-%20%235_Absolute_&_Relative_Paths_Moving_Directory.png)