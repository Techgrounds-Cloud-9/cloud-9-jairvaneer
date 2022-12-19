# What are the demands of the application?
* All VM disks need to be encrypted.
* The webserver needs daily back-ups. These back-ups need to be saved for 7 days.
*  Automate deployment of webserver.
* The admin/management server should be reachable with a public IP.
* The admin/management server should be only reachable from trusted locations (office/admin's home).
* The following IP ranges are used: 10.10.10.0/24 & 10.20.20.0/24.
* All subnets need to be protected by a firewall at subnet level.
* SSH or RDP connections to the webserver are only allowed from the admin server.
* Allow improvements to the architecture, but be decisive in order to make the deadline. 