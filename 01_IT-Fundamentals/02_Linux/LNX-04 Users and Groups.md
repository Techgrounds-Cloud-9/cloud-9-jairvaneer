# Users and Groups
Users and groups are the different clients that can be found on a computer or network, all with their own permissions. 
## Key terminology
- **Users**  
A user is and entity that can manipulate files and perform other operations withtin the OS. Each user is assigned a unique ID and has its own permissions.
- **Permissions**  
Permissions control the level of access that system processes and users have to files. 
- **Root**  
Root is the superuser account in an OS. It is a user account for administrative purposes usually, with the highest permissions of all users.  
- **Sudo**  
Short for ‘substitute user do’ or ‘super user do’. It allows a user to temporarily use root priviliges. 

 

## Exercise
### Sources
- https://www.geeksforgeeks.org/user-management-in-linux/#:~:text=A%20user%20is%20an%20entity,user%20in%20the%20operating%20system. 
- https://jfrog.com/community/devops/linux-permissions-dos-and-donts/#:~:text=What%20are%20Linux%20File%20Permissions,access%20specific%20files%20and%20directories
- https://www.beyondtrust.com/blog/entry/unix-linux-privileged-management-should-you-sudo#:~:text=Sudo%20stands%20for%20either%20%22substitute,account%20to%20have%20root%20privileges  
- https://www.cyberciti.biz/faq/add-new-user-account-with-admin-access-on-linux/ 
- https://www.hostinger.com/tutorials/linux-commands 
- https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/ 
- https://linuxize.com/post/how-to-list-groups-in-linux/ 
- https://superuser.com/questions/456762/list-admins-on-linux 

### Overcome challenges
I tried adding a user with the command `adduser jair2`, but that failed. So I tried again using the command `sudo adduser jair2` and that worked.

### Results
- Created a new user in my VM, part of an admin group, with a password and able to use sudo. ![adduser](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aae4997197b7504f40281a9e2f145e0c49d2f68b/00_includes/Sprint%201/Screenshots%20Linux/LNX-04%20Users%20and%20Groups/LNX-04%20Exercise%201%20-%20%231_Create_New_User.png)
- Found the data of my newly created user. ![userdata1](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aae4997197b7504f40281a9e2f145e0c49d2f68b/00_includes/Sprint%201/Screenshots%20Linux/LNX-04%20Users%20and%20Groups/LNX-04%20Exercise%201%20-%20%232_New_User_Data.png) ![userdata2](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/aae4997197b7504f40281a9e2f145e0c49d2f68b/00_includes/Sprint%201/Screenshots%20Linux/LNX-04%20Users%20and%20Groups/LNX-04%20Exercise%201%20-%20%232_New_User_Data_2.png)