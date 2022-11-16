# Elastic Compute Cloud (EC2)
Learning and creating an Instance with AWS EC2.

## Key terminology
RDP= Remote Desktop Protocol is a secure network communications protocol to give users access to their physical work computers.

AMI= Amazon Machine Image this provides information that is required to launch an instance. You can launch multiple instances from a single AMI, but you do have to specify each time which AMI you use for the instance you create.

EBS= Elastic Block Store provides storage in blocks which is easily accessible and can be used for long-term storage. These blocks can be used as a device(s) for the instance(s) you create, it functions the same as how you would work with a hard drive disk.

EC2= see the terminology of AWS 4.

HVM= Hardware Virtual Machine which mimics the bare-metal server setup. This instance type allows the OS to run directly on the VM without having to configure anything else.

## Exercise
- Navigate to the EC2 menu.
- Launch an EC2 instance with the following requirements:
    - AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type
    - Instance type: t2.micro
    - Default network, no preference for subnet
    - Termination protection: enabled
    - User data:
    
    #!/bin/bash
    yum -y install httpd
    systemctl enable httpd
    systemctl start httpd
    echo '<html><h1>Hello From Your Web Server!</h1></html>' >   /var/www/html/index.html
    - Root volume: general purpose SSD, Size: 8 GiB
    - New Security Group:
    Name: Web server SG
    Rules: Allow SSH, HTTP and HTTPS from anywhere

Second part of this assignment:

- Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.
- Log in to your EC2 instance using an ssh connection.
- Terminate your instance.

### Sources
https://www.techtarget.com/searchenterprisedesktop/definition/Remote-Desktop-Protocol-RDP#:~:text=What%20is%20remote%20desktop%20protocol,their%20physical%20work%20desktop%20computers.

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html

https://docs.rightscale.com/faq/What_is_Hardware_Virtual_Machine_or_HVM.html#:~:text=HVM%20(known%20as%20Hardware%20Virtual,on%20a%20real%20physical%20server.

https://www.youtube.com/watch?v=nfvR9m2ucbA

### Overcome challenges
Figuring out how to terminate with the protection enabled from the assignment. I just disabled it and refreshed the page, after that it allowed me to terminate my instance and as a safe measure I terminated all parts of the instance. They key and security group etc.

### Results
Creating the EC2 instance HVM with the specified settings, rules and user data input.

Here you see the settings for the Security Group with the rules added.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_SG_allow.png)

This is where I put the User Data input.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_user_data_input.png)

I finally confirmed the settings and launched the Instance.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_succesfully_launched_instance.png)

Here it shows that it passed the checks and that the Instance is running.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_instance.png)

I had some trouble logging in through Windows PowerShell I forgot to put the Path for the key that was needed for logging in through SSH.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_logging_in.png)

Then I executed the update after logging in.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_logged_in_updating.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_instance_updated.png)

I just wanted to see if it would display the html input from the User Data. So I went to the http with the IP address as you see here below.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_http_output.png)

Then sadly the fun was over and I had to terminate the instance and I also terminated the other resources connected to the instance.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/890c997806320876ab284d690caea41a990f60f5/00_includes/week%205/AWS%206/AWS6_instance_terminated.png)
