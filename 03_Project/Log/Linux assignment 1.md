# Linux assingment 1
Log into the Virtual Machine using the key provided.

## Key terminology
Virtual Machine - A device existing without physical form in cloud/network.
Hypervisor - Is the host and manages the guests on the VM (Virtual Machine)
ssh -i path to key username@servername -p port id

## Exercise
### Sources
https://en.wikipedia.org/wiki/Hypervisor

https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open

https://www.youtube.com/watch?v=ZcC4Eq0a5Mw

https://superuser.com/questions/1666505/how-to-set-600-permission-on-a-pem-file-in-w10

https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui

https://superuser.com/questions/1661724/how-do-i-find-my-username-and-servername-for-windows-ssh-server

### Overcome challenges
Still working on getting the key permission right, I already changed the key permission like the video in the youtube link shows. Even though it still won't allow me to access the VM. After finally figuring out that the command had to exist out of the Path to the key, username and IP adress, along with a command to get the SSH Port right. It finally allowed me to get in and typ "whoami". Screenshots can be found in 00_includes. In the end the problem I had to find a solution to wasn't how to put the key in, but how to add the port.

### Results
 After the second round in the afternoon I managed to finish the command which was needed to login and use whoami to check which user I am.

![no login](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/main/00_includes/OpenSSH%20failed%20key.png)
![key usage](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/main/00_includes/Still%20no%20access.png)
![Succes](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/main/00_includes/whoami.png)