# Cron jobs

## Key terminology
- Bash Script  
See Assignment 7, Exercise 1. 

- Cron  
Cron is a time-based system utility that can be used to schedule programs. Its name is derived from the Greek word for time, Chronos.
- Cronjob  
A cron job is a task that is executed at specified intervals. The tasks can be scheduled to run by a minute, hour, day of the month, month, day of the week, or any combination of these.  
- Crontab  
Short for cron table. It is a configuration file that holds an overview of the cronjobs. In order to execute these cronjobs crontab uses the daemon cron.

## Exercise
### Sources
- Had some trouble with printing the time and date in the file in the home directory, found out I was using the wrong bash `/bin/bash` instead of `/usr/bin/bash`.  
- Saw that the cron logs gave an error `no MTA installed, discarding output`. After searching for what that means I found that it referred to a Message Transfer Agent. So I silenced the email program with the command .................. 

### Overcome challenges


### Results
- Created a bash script that writes the current date and time to a file. ![bash time date](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2e8f455d8ed0c67d6dbb115779c272c2fc04de0b/00_includes/Sprint%201/Screenshots%20Linux/LNX-08%20Cron%20Jobs/LNX-08%20Exercise%201%20-%20%231_DateTime_Script.png) ![datetime output](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2e8f455d8ed0c67d6dbb115779c272c2fc04de0b/00_includes/Sprint%201/Screenshots%20Linux/LNX-08%20Cron%20Jobs/LNX-08%20Exercise%201%20-%20%232_DateTime.png)
- Register the script in the crontab so that it runs every minute. ![crontab](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2e8f455d8ed0c67d6dbb115779c272c2fc04de0b/00_includes/Sprint%201/Screenshots%20Linux/LNX-08%20Cron%20Jobs/LNX-08%20Exercise%201%20-%20%233_Crontab.png) ![crontab result](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2e8f455d8ed0c67d6dbb115779c272c2fc04de0b/00_includes/Sprint%201/Screenshots%20Linux/LNX-08%20Cron%20Jobs/LNX-08%20Exercise%201%20-%20%234_Cronjob_DateTime.png)
- Created a script that writes available disk space to a log file in ‘/var/logs’. Used a cron job so that it runs weekly. ![diskspace script](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2e8f455d8ed0c67d6dbb115779c272c2fc04de0b/00_includes/Sprint%201/Screenshots%20Linux/LNX-08%20Cron%20Jobs/LNX-08%20Exercise%201%20-%20%235_DiskSpace_Script.png) ![iskspace crontab](https://github.com/Techgrounds-Cloud-9/cloud-9-jairvaneer/blob/2e8f455d8ed0c67d6dbb115779c272c2fc04de0b/00_includes/Sprint%201/Screenshots%20Linux/LNX-08%20Cron%20Jobs/LNX-08%20Exercise%201%20-%20%235_Crontab_2_Jobs.png)
