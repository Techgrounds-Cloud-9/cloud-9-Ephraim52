# IP-Addressing
An introduction to how IP-adresses work and the differences between private and public addresses.

## Key terminology
IPv4= Internet Protocol version 4 using a 32-bit address space it is one of the core protocols of standards-based internetworking.

IPv6= Internet Protocol version 6 is a successor to the IPv4 using 128-bit addresses it does the same as IPv4 but has more address space and as such can provide more than the IPv4 can.

NAT= Network Address Translation it is a way of filing an IP Address space into another through modifying a network address's information in the IP Header of the packets.

Static address= An IP address that doesn't change. Untill the device is decommissioned or your network architecture changes.

Dynamic address= Are assigned by the DHCP when they are needed when IPv4 doesn't provide enough static addresses.

Public address= This is the address that your device uses through your modem/router to identify your device on the Public internet and is external as such.

Private address= This address is the one you use locally because it is internal in your Local Area Network (LAN) and is not used on the Public internet to identify yourself with to another device or website.

Octet= Is a piece of an internet address public and private: 192.168.178.112 each 3 numbers before the dot represents an octet a piece of the IP address.

DHCP= Dynamic Host Configuration Protocol

## Exercise
- Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.
- Zijn de adressen hetzelfde of niet? Leg uit waarom.
- Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
- Zijn de adressen hetzelfde of niet? Leg uit waarom.
- Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?
- Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?

### Sources
https://en.wikipedia.org/wiki/Network_address_translation

https://en.wikipedia.org/wiki/IPv4

https://en.wikipedia.org/wiki/IPv6

https://www.avast.com/c-static-vs-dynamic-ip-addresses#:~:text=A%20static%20IP%20address%20is,servers%20or%20other%20important%20equipment.

https://www.digitalcitizen.life/find-public-ip-address/#ftoc-heading-2

https://store.jcrinc.com/assets/1/7/What_is_My_IP_Address.pdf

https://www.guru99.com/how-to-change-ip-address.html

https://www.businessinsider.com/guides/tech/how-to-change-your-ip-address?international=true&r=US&IR=T

https://www.businessinsider.com/guides/tech/how-to-change-ip-address-on-android?international=true&r=US&IR=T

### Overcome challenges
No challenges so far, I'm very (ec)static!

### Results
This is the public IP address of my laptop & mobile phone:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/NTW-05_public_ip.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/Screenshot_20221004-101100_Chrome.jpg)

The addresses are not the same because each device gets assigned their own static IP address through the Internet Protocol version 4 from the DHCP. If they would all have the same addresses then the connection would be unstable due to the conflict of everyone having the same address.

This is the private IP address of my laptop & mobile phone:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/NTW-05_ip_address_laptop_phone.png)

The addresses are the same in the first 3 octets only the last octet changes up to 255 because thats the amount available on IPv4. Two devices each their own address through the last octet being different.

Changed my mobile its private IP address to my laptop its address:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/Screenshot_20221004-105747_Settings.jpg)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/NTW-05_ip_address_laptop_phone.png)

My mobile phone is connected but when using the browser doesn’t respond as fast to finding a specified website.

Changed my ip address of my mobile to an address outside my local area network:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/Screenshot_20221004-110616_Settings.jpg)

When changing the private IP address to a public IP address my mobile seems to have lost connection. As the webbrowser doesn’t load.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/10579e1223d13e876763f151442f635873f45cbf/00_includes/week%202/assignment%205/Screenshot_20221004-110827_Chrome.jpg)
