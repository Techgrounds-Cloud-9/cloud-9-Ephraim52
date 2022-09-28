# Processes
Running daemons, services, programs in Linux.

## Key terminology
Daemon = runs in the background and is non-interactive

Services= responds to requests from programs

Program= A program is used and run by users program like (vim or nano)

PID = Process ID number, the identity of the process

Sudo apt-get install telnetd -y = command to install telnet daemon

Systemctl status inetd= verifies the installation, shows PID, memory usage and status active/not active

Logout= loggin out to close the connection

Systemctl stop inetd= command to stop the process


## Exercise
### Sources
https://www.youtube.com/watch?v=l7T7UEGqnoo

https://www.javatpoint.com/linux-telnet-command

https://store.chipkin.com/articles/telnet-how-do-i-end-a-telnet-session-windows-linux-mac

### Overcome challenges
The beginning was hard when I had to figure out how to get telnet daemon active after figuring out that I had to install it. I read through the sources that I found and as you see in Key terminology I used these commands to get the assignments done for this exercise.

### Results
These images show the results that I had for this exercise.

The first image you see that I am installing telnet.

In the second image you that the telnet daemon is active, the PID 7706 and the memory usage 856.0K.

The third image shows that I stopped the telnet process. As it shows as inactive.

![alt text]()

![alt text]()

![alt text]()