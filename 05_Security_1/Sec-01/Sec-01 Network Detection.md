# Network Detection
How to check and secure you network.

## Key terminology
Found none.

## Exercise
- Scan the network of your Linux machine using nmap. What do you find?
- Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser. (Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)

### Sources
https://itsfoss.com/how-to-find-what-devices-are-connected-to-network-in-ubuntu/

### Overcome challenges
Only finding out in the Linux machine which IP address was mine. Used various commands to get different results till I found my own.

### Results
At the first part I scanned the host and found all my fellow students on the same Network. Later on I used the other IP address and found only myself and more hosts.

![alt text]()

![alt text]()

Now I checked only my assigned IP address and only this came up:

![alt text]()

It is sending packets back and forth when opening a browser and surf a bit. As well as turning off the webcam it sends less packets.

![alt text]()

![alt text]()