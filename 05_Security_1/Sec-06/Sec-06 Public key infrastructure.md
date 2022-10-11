# Public Key Infrastructure
Analyze the roles, policies, hardware, software, procedures needed to create, manage, distribute, use, store, revoke digital certificates and manage public key encryption.

## Key terminology
PKI= Public key infrastructure its purpose is serve as a secure electronic transfer of information for various network activities.

SSL= Secure Sockets Layer to keep internet connections secure and protect data from being stolen by hackers or other people with harmful intentions.

## Exercise
- Create a self-signed certificate on your VM.
- Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
- Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).

### Sources
https://linuxize.com/post/creating-a-self-signed-ssl-certificate/

https://en.wikipedia.org/wiki/Public_key_infrastructure

https://www.openssl.org/docs/man1.0.2/man1/openssl-req.html

https://www.keyfactor.com/resources/how-to-check-ssl-certificate/#:~:text=To%20check%20an%20SSL%20certificate,information%20related%20to%20the%20certificate.

https://betterstack.com/community/questions/how-to-list-all-available-ca-ssl-certificates-on-ubuntu/

http://woshub.com/updating-trusted-root-certificates-in-windows-10/

https://www.websecurity.digicert.com/security-topics/what-is-ssl-tls-https#:~:text=SSL%20stands%20for%20Secure%20Sockets,transferred%2C%20including%20potential%20personal%20details.

### Overcome challenges
Struggled to specify the code for the VM to create a key. Solved after discussing my issue with teammates who told me I was on the right track.

### Results
The certificates are easier to find through commands in a terminal than looking up manually in a graphical user interface, where you check them individually. 

For websites certificates they are very clear in google for a website you can see a good overview on what version the certificate is and all other properties that belong to it.

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()