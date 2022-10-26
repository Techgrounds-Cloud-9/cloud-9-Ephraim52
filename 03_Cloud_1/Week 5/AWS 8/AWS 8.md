# Security Groups
Learn what Security Groups and NACL is as well as what it is used for.

## Key terminology
VPC= Virtual Private Cloud is a virtual network in our case for AWS, but could also be Azure or Google. This network is isolated from other virtual networks and you can set a range of IP addresses for the VPC to add subnets, security groups and gateways.

ELB= Elastic Load Balancer an automated process for dividing incoming traffic over multiple targets. It sends the traffic only to healthy targets and scales the capacity automatically in response to incoming traffic. Increases availability and makes it less prone to fault, as well as flexibel you can adjust it to your needs by adding and removing compute resources.

## Exercise
- Security Groups in AWS
- Network Access Control Lists in AWS

### Sources
https://www.checkpoint.com/cyber-hub/cloud-security/what-is-aws-security-groups/

https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html

### Overcome challenges
Love reading! <3

### Results
AWS Security Groups are virtual firewalls much like VM's. They can be used to control in- and outgoing traffic, you set rules for this in the Security Group that controls the flow of in- and outgoing traffic. Every Instance in AWS EC2 needs a Security Group assigned to it, each Group can have different rules. These groups are Stateful because if an inbound request passess then the outbound request will pass as well.

AWS Network Acces Control Lists are stateless as they check both in- and outbound traffic. This is an extra option to add as an extra security meassure, it also controls traffic for one or more subnets.