# Protocols
Learning how to identify protocols understand what they are and in which layer they are in.

## Key terminology
UDP= User Datagram Protocol, a communication protocol that speeds up communications for allowing data to be transferred faster.

Wireshark= Open source packet analyzer for network troubleshooting and analysis. 

DNS= Domain Name System, is a set of protocols and standards. Turns long IP adresses into user-friendly URL's.

## Exercise
- Identify several other protocols and their associated OSI layer. Name at least one for each layer.
- Figure out who determines what protocols we use and what is needed to introduce your own protocol.
- Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

### Sources

https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/

https://en.wikipedia.org/wiki/Wireshark

https://www.techopedia.com/definition/24961/osi-protocols

https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/

https://www.geeksforgeeks.org/protocol-and-standard-in-computer-networks/

https://computer.howstuffworks.com/internet/basics/who-owns-internet2.htm

https://stackoverflow.com/questions/18249847/how-to-build-a-protocol-on-top-of-tcp

https://www.quora.com/How-would-one-create-and-implement-their-own-networking-protocol

### Overcome challenges
I didn't experience any challengs for this assignment.

### Results
Here is an image of the protocols and their associated OSI layers:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/db07a95f148fcf65252d597c5a8769c6e9594a73/00_includes/week%202/assignment%203/NTW-03_protocols_osi_level.png)

The organisations that determine what protocols we use are:

- World Wide Web Consortium (W3C)
- Telecommunication Standardization Sector (ITU-T)
- Internet Architecture Board (IAB)
- Internet Assigned Numbers Authority (IANA)
- Internet Corperation for Assigned Names and Numbers (ICANN)
- Internet Engineering Task Force (IETF)
- Internet Society (ISOC)
- Internet Research Task Force (IRTF)

They all collaborate with eachother to develop and evolve the protocols. As they set the standards that we have today for Internet Protocols & more.

For introducing your own protocol it needs to be accepted by an IETF working group. Aside of that the protocol you want to introduce needs to be a specification that defines the data you send.

Here I captured some of my network data with the protocol UDP:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/db07a95f148fcf65252d597c5a8769c6e9594a73/00_includes/week%202/assignment%203/NTW-03_capture_protocol.png)

UDP a datagram is a method to transfer data between two devices in a network. Without having to establish a connection first, it can send packets directly. This is a faster way of transferring data but less reliable as it does not check if a packet arrived as intended.

Here you see that compared to TCP UDP does not check or syncronize with the other device that receives the data. Also called a handshake.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/db07a95f148fcf65252d597c5a8769c6e9594a73/00_includes/week%202/assignment%203/NTW-03_TCP_vs_UDP.png)
