#!/bin/bash
sudo yum install httpd -y
sudo service httpd start
sudo service httpd enable
sudo echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html