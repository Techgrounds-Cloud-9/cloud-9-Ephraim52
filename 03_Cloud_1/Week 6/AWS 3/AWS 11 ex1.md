# Elastic Load Balancing (ELB) & Auto Scaling
What is ELB and how it works, learning its functions, benefits and how to apply it.

## Key terminology
CloudWatch= A service that monitors your resources and applications you run in AWS in real time. To collect measurements of your resources and applications to display the metrics. Cloudwatch can also be used to make alarms that can automatically make changes to the resources it monitors.(SaaS)

ELB= Elastic Load Balancing is a load balancing service which automatically distributes incoming application traffic and scales the resources according to the traffic.(SaaS)

Four types of ELBs:
- Application Load Balancer: this ELB works using HTTP and HTTPS protocols (layer 7 of the OSI stack).
- Network Load Balancer: this ELB works using TCP and UDP (layer 4 of the OSI stack).
- Classic Load Balancer: this ELB is outdated and not recommended for use. AWS has (so far) never stopped supporting any services. The reason for this is that it can harm existing applications.
- Gateway Load Balancer: this ELB acts as a gateway into your network, as well as a load balancer. It will first route traffic to a (3rd party) application that checks the traffic, like an IDS/IPS or Firewall. After the packet has been inspected, the GWLB acts like a NLB routing to your application. GWLB act on layers 3 and 4 of the OSI stack.

## Exercise 1
- Launch an EC2 instance with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - AMI: Amazon Linux 2
    - Type: t3.micro
    - User data:
#!/bin/bash
yum install -y httpd mysql php
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
chkconfig httpd on
service httpd start
    - Security Group: Allow HTTP
- Wait for the status checks to pass.
- Create an AMI from your instance with the following requirements:
- Image name: Web server AMI    

### Sources
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html

https://www.techtarget.com/searchaws/definition/elastic-load-balancing#:~:text=Elastic%20Load%20Balancing%20(ELB)%20is,incoming%20application%20and%20network%20traffic.

### Overcome challenges
Had to make a subnet as I think I delete the default subnet by mistake when deleting all the resources from assignment AWS 10.

### Results
Here I made the instance with the settings and input.

![alt text]()

Here I created an image from the instance I made.

![alt text]()
