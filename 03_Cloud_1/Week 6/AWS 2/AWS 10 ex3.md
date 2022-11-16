# Virtual Private Cloud (VPC)
How a VPC operates and its functions to learn how it works as well as what it is.

## Key terminology
VPC= Virtual private cloud is an isolated network/VM where you control access and isn't available to the public.

## Exercise 3
- Create a Security Group with the following requirements:
    - Name: Web SG
    - Description: Enable HTTP Access
    - VPC: Lab VPC
    - Inbound rule: allow HTTP access from anywhere
    - Outbound rule: Allow all traffic

### Sources
https://www.youtube.com/watch?v=NN8JSRCBNB8

https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html

https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

### Overcome challenges
None making security groups is pretty clear as well as why you need them.

### Results
Here I made the security group called Web SG, with the following rules.

Inbound:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/f4760dc8fbdf47f849afc4005cbf270ef02c5a6d/00_includes/week%206/AWS%2010/AWS10_ex3_inbound.png)

Outbound:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/f4760dc8fbdf47f849afc4005cbf270ef02c5a6d/00_includes/week%206/AWS%2010/AWS10_ex3_outbound.png)
