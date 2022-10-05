# Subnetting
Learn to create and understand your own subnet.

## Key terminology
CIDR notation= Classless Inter-Domain Routing, its a representation of an IP address and its associated network.

Subnet= A subnet divides a larger network into smaller networks. The subnet being the the smaller network.

## Exercise
Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
- 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.
- 1 private subnet dat internet toegang heeft via een NAT gateway. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).
- 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts    kunnen plaatsen (de 5 hosts is exclusief de internet gateway).
- Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.


### Sources
https://www.techtarget.com/searchnetworking/definition/subnet#:~:text=A%20subnet%2C%20or%20subnetwork%2C%20is,to%20another%20over%20the%20internet.

https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation

https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html

https://www.youtube.com/watch?v=SBYNeGIng6I

https://www.youtube.com/watch?v=fTTfbxrYRE4

https://www.1cloudhub.com/aws-vpc-101-creation-of-public-subnet-and-private-subnet-in-vpc-and-test-connectivity/#:~:text=A%20private%20subnet%20is%20a,the%20traffic%20from%20the%20internet.

https://www.calculator.net/ip-subnet-calculator.html?cclass=c&csubnet=26&cip=192.168.50.0&ctype=ipv4&printit=0&x=72&y=20

https://docs.axway.com/bundle/SecureTransport_54_on_AWS_InstallationGuide_allOS_en_HTML5/page/Content/AWS/securitygroups/st_nat_gateway_subnet_routing.htm#:~:text=Navigate%20to%20Virtual%20Private%20Cloud,Click%20Create%20a%20NAT%20Gateway.

### Overcome challenges
Figuring out how to add a NAT Gateway and going from private to public. Just need to read through a lot of information from different sources to have the best understanding.

### Results
The first part I made 4 subnets with 64 hosts available minus 2 because of the IP address itself and the broadcast address. Like in- and outgoing. It is basically dividing your Local area network in 4 which comes down to the 64 available IP addresses that you can assign or let users use.

For the second part I took one of the subnets as an example on continueing with the remaining subnets that I had available from the example in the first part.

For the third I simply used the third subnet and added an internet gateway as you can set that through settings on your operating system. All subnets have 62 hosts available and you can set their seperate addresses through IPv4.

![alt text]()