# Asymmetric encryption
What does Asymmetric encryption mean and what does it do?

## Key terminology
Asymmetric encryption= Is a way to ensure that only the receiver can read the message. By encrypting the public key, the private key would be used for decrypting and we all know private means only one person has that key. 

RSA= Rivest-Shamir-Adleman is a cryptographic algorithm uses a private and public key that makes it asymmetric.

## Exercise
- Generate a key pair.
- Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.

### Sources
https://www.techtarget.com/searchsecurity/definition/asymmetric-cryptography#:~:text=Asymmetric%20encryption%20uses%20a%20mathematically,key%20is%20used%20for%20decryption.

https://www.practicalnetworking.net/series/cryptography/using-asymmetric-keys/

https://security.stackexchange.com/questions/101560/how-to-securely-send-private-keys#:~:text=The%20proper%20way%20to%20do,Private%20Key%20and%20send%20it.

https://stackoverflow.com/questions/13476355/how-does-rsa-distribute-keys-to-the-sender-and-receiver

https://simple.wikipedia.org/wiki/RSA_algorithm#:~:text=RSA%20(Rivest%E2%80%93Shamir%E2%80%93Adleman,can%20be%20given%20to%20anyone.

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results
Asymmetric is more secure as the chance that the data could be intercepted is less present. Here Daphne shared her Public Key with me so I could encrypt my message. She then decrypted the message I send through slack with her Private Key.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/8607f9fb899467257eebc99c715079b76c80fdbe/00_includes/week%203/assignment%203/Sec-05_slack_PK.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/8607f9fb899467257eebc99c715079b76c80fdbe/00_includes/week%203/assignment%203/Sec-05_message.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/8607f9fb899467257eebc99c715079b76c80fdbe/00_includes/week%203/assignment%203/SEC05_screenshot_dominic_message.png)
