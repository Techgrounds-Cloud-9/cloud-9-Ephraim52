# File permissions
Adding and removing file permissions for user & groups.

## Key terminology
Usermod -G superheros ironman = add existing user to the group also -g like this is primary group and -G is secondary and anything beyond that
R= read permission
W= writing permission
X= execute permission
-= no permission
Chmod permissions filename= change mode, set permissions. You can also set permissions numerical.
Chmod 764 filename
Ls -l shows list of files with owners and permissions
+ = adds permission
-= removes permission
= sets permissions and overrides the permissions earlier set
U = user
G = group
O = other
A = all
Chown user filename= change owner of the file
Chown user:group filename= change owner and group of the file

## Exercise
### Sources
https://www.youtube.com/watch?v=D-VqgvBMV7g

### Overcome challenges
While making notes of the video I understood how to execute the commands and had no issues with the assignment on how to execute it.

### Results
A new text file which no one but the assigned user and group have access to. While trying to read it from my user I was denied just like the assignment intended as shown in one of the images below.

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()