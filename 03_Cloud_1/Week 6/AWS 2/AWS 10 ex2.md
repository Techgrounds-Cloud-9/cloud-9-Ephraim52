# Virtual Private Cloud (VPC)
How a VPC operates and its functions to learn how it works as well as what it is.

## Key terminology
VPC= Virtual private cloud is an isolated network/VM where you control access and isn't available to the public.

## Exercise 2
- Create an additional public subnet without using the wizard with the following requirements:
    - VPC: Lab VPC
    - Name: Public Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.2.0/24
- Create an additional private subnet without using the wizard with the following requirements:
    - VPC: Lab VPC
    - Name: Private Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.3.0/24
- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.
- Explicitly associate the private route table with your two private subnets.
- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.
- Explicitly associate the public route table to your two public subnets.

### Sources
https://www.youtube.com/watch?v=NN8JSRCBNB8

https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html

https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

### Overcome challenges
Had to manually make the NAT gateway as I forgot to attached it during the creation options of the VPC. I read some information on how to make it and attach it properly to the specified route table.

### Results
I made the extra subnets for availability zone 2 as you can see in this screenshot:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/421eedc22421b151bc28bf26e8cb28360445d96e/00_includes/week%206/AWS%2010/AWS10_ex2_new_subnets_az2.png)

Then I made checked the route tables, though there was none that had a NAT gateway attached to it. So I made the NAT gateway myself and assigned it to the main route.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/421eedc22421b151bc28bf26e8cb28360445d96e/00_includes/week%206/AWS%2010/AWS10_ex2_route_tables.png)
