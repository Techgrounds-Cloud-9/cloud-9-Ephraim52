# Passwords
How passwords are protected and how they can get leaked.

## Key terminology
hashing= Is a way to turn your password into a string of character/or numbers by using an encryption algorithm.

Salting= This adds a string of 32 or more characters and then hashing them. Its used to protect passwords from reverse-engineering passwords as this adds an extra layer of security combining the salt string and hash string together.

Rainbow table= Is a database that has a directory filled with plaintext passwords and their corresponding has values. When used is looks for the corresponding hash value as that is the only thing needed to crack a hashed password.

## Exercise
- Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
- Find out how a Rainbow Table can be used to crack hashed passwords.
- Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
03F6D7D1D9AAE7160C05F71CE485AD31
03D086C9B98F90D628F2D1BD84CFA6CA
- Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
- Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.


### Sources
https://delinea.com/blog/how-do-passwords-work#:~:text=Hashing%20turns%20your%20password%20

https://www.darkreading.com/risk/safely-storing-user-passwords-hashing-vs-encrypting

https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/

https://www.techtarget.com/searchsecurity/definition/salt#:~:text=What%20is%20password%20salting%3F,stealing%20them%20from%20the%20database.

https://cyberhoot.com/cybrary/password-salting/

https://www.geekyhacker.com/2021/04/11/verify-a-users-password-in-linux/

### Overcome challenges
Nothing encountered.

### Results
Where symmetric encryption stores the plaintext behind an encryption is stil has a risk of leaving the plaintext visible. Where hashing only leaves the hashed value and not the plaintext in a database.

Rainbow table is a database that has a directory filled with plaintext passwords and their corresponding has values. When used is looks for the corresponding hash value as that is the only thing needed to crack a hashed password.

Used Crackstation link to crack both MD5 hashes

![alt text]()

![alt text]()

New user made in the VM

![alt text]()

Password hash in the VM

![alt text]()

The result in the crackstation website

![alt text]()

The hashes of both our passwords are different because they are salted this adds an extra string of characters to the hash as it combines the two of them into the hash string. Which can't be cracked with a Rainbow table because it only uses Hashing excluding the Salt.