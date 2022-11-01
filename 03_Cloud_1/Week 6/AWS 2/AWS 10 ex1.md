# Virtual Private Cloud (VPC)
How a VPC operates and its functions to learn how it works as well as what it is.

## Key terminology
VPC= Virtual private cloud is an isolated network/VM where you control access and isn't available to the public.

Route tables= Exists out of rules that are Routes which are used to direct where network traffic from a subnet or gateway is directed towards.

## Exercise 1
- Allocate an Elastic IP address to your account.
- Use the Launch VPC Wizard option to create a new VPC with the following 

requirements:
- Region: Frankfurt (eu-central-1)
- VPC with a public and a private subnet
- Name: Lab VPC
- CIDR: 10.0.0.0/16

Requirements for the public subnet:
- Name: Public subnet 1
- CIDR: 10.0.0.0/24
- AZ: eu-central-1a

Requirements for the private subnet:
- Name: Private subnet 1
- CIDR: 10.0.1.0/24
- AZ: eu-central-1a

### Sources
https://www.youtube.com/watch?v=NN8JSRCBNB8

https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html

https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC

https://medium.com/awesome-cloud/aws-vpc-route-table-overview-intro-getting-started-guide-5b5d65ec875f#:~:text=A%20route%20table%20contains%20a,to%20get%20to%20their%20destination.

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results
First I made the elastic IP with default settings and just a name tag to recognize it faster.

![alt text]()

Then I created the VPC using the VPC with more options, this way I could create the subnets too. By unfolding the other options I could change the CIDR notation of the subnets too.

![alt text]()

The subnets:

![alt text]()

To match the infrastructure image of the VPC for the first part of the assignment I had to make a NAT gateway with the elastic IP as well, which you can see here:

![alt text]()
