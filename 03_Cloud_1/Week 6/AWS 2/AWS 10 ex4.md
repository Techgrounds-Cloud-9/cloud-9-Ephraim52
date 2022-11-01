# Virtual Private Cloud (VPC)
How a VPC operates and its functions to learn how it works as well as what it is.

## Key terminology
VPC= Virtual private cloud is an isolated network/VM where you control access and isn't available to the public.

## Exercise 3
- Launch an EC2 instance with the following requirements:
    - AMI: Amazon Linux 2
    - Type: t3.micro
    - Subnet: Public subnet 2
    - Auto-assign Public IP: Enable
    - User data:
#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql php
# Download Lab files
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
# Turn on web server
chkconfig httpd on
service httpd start
- Tag:
- Key: Name
- Value: Web server
- Security Group: Web SG
- Key pair: no key pair
- Connect to your server using the public IPv4 DNS name.

### Sources
https://www.youtube.com/watch?v=NN8JSRCBNB8

https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html

https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

### Overcome challenges
Connecting to the Public IPv4 DNS name gives an error. Needed to put http:// infront of the web address.

### Results
Here I made the EC2 instance with the required settings and input for user data.

![alt text]()

Then I connected and as mentioned has issues connecting due to having to specify http:// infront of the web address.

![alt text]()
