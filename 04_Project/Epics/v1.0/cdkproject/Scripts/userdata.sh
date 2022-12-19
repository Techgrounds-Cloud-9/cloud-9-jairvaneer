#!/bin/bash
sudo yum update -y
sudo yum -y install httpd
sudo service httpd start
sudo service httpd enable
sudo echo "<html><h1>Yes It Works!</h1></html>" >   /var/www/html/index.html