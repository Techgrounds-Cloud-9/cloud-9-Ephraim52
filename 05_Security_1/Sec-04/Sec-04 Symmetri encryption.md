# Symmetric encryption
Understanding how to encrypt data and send it in a secure way.

## Key terminology
Symmetric encryption= A form of encrypting/decrypting your data/file using a single key.

Caesar cipher= An encryption technique which Julius Caesar used for encrypting his messages. You use it by replacing the original letter in your text by for example 4 steps back in the alphabet. A, B, C, D, E, F: D would be Z for example as that would be 4 steps back from the letter in the text with E starting at A.

Plaintext= Unencrypted information that can still be encrypted.

Keystream= Is a stream of random characters combined with plaintext message makes an encrypted message.

Ciphertext= Is the result of encrypting the plaintext using an algorithm, this prevents the loss of sensitive information.

Diffie-Hellman= this is a method of exchanging keys in a secure way allowing to share key on an insecure channel using a symmetric key.

AES= Advanced Encryption Standard is a variant of Rijndaels block cipher, is the standard way for securing data/plaintext.

Block cipher= Is an algorithm that uses a group of bits.

## Exercise
- Find two more historic ciphers besides the Caesar cipher.
- Find two digital ciphers that are being used today.
- Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. 
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.

### Sources
https://www.sciencedirect.com/topics/computer-science/symmetric-encryption#:~:text=Symmetric%20encryption%20uses%20a%20single,kept%20secret%20from%20third%20parties.

https://en.wikipedia.org/wiki/Caesar_cipher

https://www.theguardian.com/childrens-books-site/2015/sep/10/top-10-codes-keys-and-ciphers

https://www.keyfactor.com/blog/cipher-suites-explained/

https://cheapsslsecurity.com/p/everything-you-need-to-know-about-an-ssl-cipher-cipher-lists/

https://www.uvic.ca/systems/support/informationsecurity/fileencryption/encryptfile7zip.php

https://setapp.com/how-to/password-protect-zip

https://www.php.net/manual/en/function.password-hash.php

https://www.baeldung.com/cs/symmetric-cryptography

https://crypto.stackexchange.com/questions/10371/how-is-the-key-shared-in-symmetric-key-cryptography#:~:text=Symmetric%20keys%20should%20be%20kept,secret%2C%20as%20privacy%20implies%20secrecy.

https://www.ibm.com/docs/en/zos/2.3.0?topic=pdk-using-rsa-public-keys-protect-keys-sent-between-systems

https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/create-identical-symmetric-keys-on-two-servers?view=sql-server-ver16

https://www.youtube.com/watch?v=ERp8420ucGs

https://www.youtube.com/watch?v=10BX3zOr7wk

https://en.wikipedia.org/wiki/Plaintext

https://en.wikipedia.org/wiki/Keystream

https://en.wikipedia.org/wiki/Ciphertext

https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

https://en.wikipedia.org/wiki/Advanced_Encryption_Standard

https://en.wikipedia.org/wiki/Block_cipher

https://www.techrepublic.com/article/solving-the-key-exchange-problem/

https://www.dcode.fr/caesar-cipher

### Overcome challenges
Deciding on which cipher to use and in which order to add this for encrypting the key.

### Results
Two other historic encryption ciphers:

The use of Hieroglyphs and the Enigma machine.

- Hieroglyphs used by the Egyptians as their way of writing.

- The Enigma machine used by the Germans in World War 2 for encrypting their messages. Looking like a typing machine it was designed and set to code messages.

Two digital ciphers still being used today:

TLS and SSL, both share similarities.

For the last part of this exercise I transferred my excel sheet into an encrypted .zip file. The password being encrypted with a cipher and a slight hint in the .zip file name.

After doing the Asymmetric exercise we used the same public key to encrypt and decrypt. We send a message in Caesar's cipher with a shift of 10 meaning that if I wrote A it would be K. We used the Caesar's cipher website to decrypt the cipher that was in the encrypted message.

This was the message in Caesar's cipher XUBBE WYJKF, which when decrypted using the right cipher and key reads Hello Gitup.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/974184d98d5628457b24a54c7a7cba6eed7c3d67/00_includes/week%203/assignment%202/SEC04_screenshot_caesar_keygen.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/974184d98d5628457b24a54c7a7cba6eed7c3d67/00_includes/week%203/assignment%202/SEC04_screenshot_caesar.png)
