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

## Exercise 3
- Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
- Create an auto scaling group with the following requirements:
    - Name: Lab ASG
    - Launch Configuration: Web server launch configuration
    - Subnets: must be in eu-central-1a and eu-central-1b
    - Load Balancer: LabELB
    - Group metrics collection in CloudWatch must be enabled
    - Group Size:
        - Desired Capacity: 2
        - Minimum Capacity: 2
        - Maximum Capacity: 4
    - Scaling policy: Target tracking with a target of 60% average CPU utilisation

### Sources
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html

https://www.techtarget.com/searchaws/definition/elastic-load-balancing#:~:text=Elastic%20Load%20Balancing%20(ELB)%20is,incoming%20application%20and%20network%20traffic.

### Overcome challenges
Had to make a subnet as I think I delete the default subnet by mistake when deleting all the resources from assignment AWS 10.

The other part was creating the load balancer where the steps would be the other way around. First I had to make the Security group and Target Group, after that I could create the Load balancer. Otherwise it wouldn't seem to find the Security group for example.

### Results
Launch template instead of launch configuration:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/1e3314b9cdc1dd82ca6d16412bdfeed35e96b1e8/00_includes/week%206/AWS%2011/AWS11_ex3_launch.png)

Scale group created:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/1e3314b9cdc1dd82ca6d16412bdfeed35e96b1e8/00_includes/week%206/AWS%2011/AWS11_ex3_scaling_group.png)
