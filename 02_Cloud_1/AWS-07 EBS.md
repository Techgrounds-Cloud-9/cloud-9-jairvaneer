# EBS
EBS are similar to virtual hard drives in the cloud, used for storage. 
## Key terminology
- **EBS**  
Short for Elastic Block Store. This is a block-storage service from AWS made for EC2.  
- **Block-Storage**  
This is a type of storage where the data is seperated in multiple "blocks" which are all the same size. . The blocks receive an unique adress which matches to the saved data. When calling the data the computer checks the adresses to find the right files.
- **EBS Multi-Attach**  
A AWS service that enables clients to attach one volume to multiple instances that are ion the same availability zone. Multi-Attach makes it easier for you to achieve higher application availability in clustered Linux applications that manage concurrent write operations.

## Exercise
### Sources
- https://aws.amazon.com/ebs/  
- https://www.true.nl/blog/verschillen-file-storage-block-storage-en-object-storage/  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html    
- https://n2ws.com/blog/how-to-guides/connect-aws-ebs-volume-another-instance  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html#umount-detach-volume  
- https://devconnected.com/how-to-mount-and-unmount-drives-on-linux/  
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html

### Overcome challenges
The first time I created the second volume I could not connect it to the instance. By looking into the volume I created it showed that it was placed in a different availability region.

### Results
- Created an instance and a new volume.  
![Launch Instance](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%201%20-%20%231_Launch_Instance.png)  
![status available](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%201%20-%20%232%20Status_Available.png)  
- Attached the volume to the instance. After that, using `lsblck` I checked to see the volume connected but not mounted, it was named `/dev/xvdf`. Created a new mountpoint by inputting `mkdir /mountdir`, after which I mounted the volume to it by inputting `mount /dev/xvdf /mountdir`. After navigating to the mountpoint, `cd /mountdir`, a textfile was created with some text by inputting `echo "This is the text file in the mounted volume"> textfile.txt`.  
![text file mounted volume](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%202%20-%20%231_Text_File_Mounted_Volume.png)  
- Created a snapshot of the EBS volume.  
![snapshot](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%203%20-%20%231_Snapshot.png)  
- Removed the text file from the original volume and created a new volume with the snapshot, after which I unmount and detached the original volume
![unmount volume](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%203%20-%20%233_Unmount_Volume.png)  
- Attached the new volume.  
![attach new volume](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%203%20-%20%234_Attach_New_Volume.png)
- Mounted the new volume.  
![mounted new volume](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%203%20-%20%235_Mounted_New_Volume.png)
- Found the text file.  
![found text file](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/a28f3d1b76d26d081533ade05af8b4d403804c4b/00_includes/Sprint%204/Screenshots%20AWS/AWS-07/AWS-07%20Exercise%203%20-%20%236_Found_Old_Textfile.png)  
- Terminated the instance and volumes.
