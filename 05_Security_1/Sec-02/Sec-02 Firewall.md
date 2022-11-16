# Firewall
learning about firewalls and what they do. How firewalls work.

## Key terminology
Stateful firewall= This firewall monitors the full state of active network connections, so it is constantly analyzing the complete contents of the traffic and data packets when seeking entry to a network.

Stateless firewall= Does not inspect traffic, instead looks if the packets are conform with the security rules. This kind of firewall protects you less than the stateful firewall.

CentOS= Community Enterprise Operating System is a Linux distribution providing open-source community supported computing platform.

iptables= Is a part of the Linux kernel firewall the iptables set up, maintain and inspect the tables of IPv4 and IPv6 to filter packet rules.

## Exercise
- Installeer een webserver op je VM.
- Bekijk de standaardpagina die met de webserver geïnstalleerd is.
- Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.
- Controleer of de firewall zijn werk doet.

### Sources
https://www.cyberciti.biz/faq/how-to-configure-firewall-with-ufw-on-ubuntu-20-04-lts/

https://www.makeuseof.com/tag/set-apache-web-server-3-easy-steps/

https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server

https://www.n-able.com/blog/stateful-vs-stateless-firewall-differences#:~:text=A%20stateful%20firewall%20is%20a,and%20data%20packets%20in%20isolation.

https://www.cdw.com/content/cdw/en/articles/security/stateful-versus-stateless-firewalls.html#:~:text=Stateless%20firewalls%20do%20not%20inspect,a%20suitable%20level%20of%20protection.

https://en.wikipedia.org/wiki/CentOS

I used man iptables to look up the description in Linux.

### Overcome challenges
In my Linux machine the firewall seemed to be inactive. Looked for information about how to activate this had to use the sudo ufw enable command, I checked this by using man ufw which showed all the options and explained all options as well. 

Couldn't seem to get into the website I made on Linux, but in the end I found out I needed the public ip instead of the hostname ip.

### Results
First part was installing and setting up Apache after that I checked the standard webpage in the editor to be sure everything was ok. To configure the firewall settings I had to use sudo ufw commands.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/3aa23bf0d0c632d06a1e7237823d84d6f58f10bf/00_includes/week%202/assignment%208/Sec-02_default_website_linux.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/3aa23bf0d0c632d06a1e7237823d84d6f58f10bf/00_includes/week%202/assignment%208/Sec-02_allowing_access.png)

Here you see the website how I wrote it in Linux and a view of the website online with just some text. To achieve this I made a few seperate new files: content.html (contains the html code for the website) and host_example.conf. Along with the directories host_example and html which is located in /var/www/host_example/html/content.html is the absolute path. For finding the website in the webbrowser I used the public IP address of the host along with the port.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/3aa23bf0d0c632d06a1e7237823d84d6f58f10bf/00_includes/week%202/assignment%208/Sec-02_html_content.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/3aa23bf0d0c632d06a1e7237823d84d6f58f10bf/00_includes/week%202/assignment%208/Sec-02_myownwebsite.png)

The firewall is now blocking traffic while allowing ssh connection and checking the website:

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/3aa23bf0d0c632d06a1e7237823d84d6f58f10bf/00_includes/week%202/assignment%208/Sec-02_deny_access.png)
