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
minus= (-) removes permission
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

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/7bc574b8dfa7a952c463e81fd74e57fc58219b9a/00_includes/week%201/assignment%207/file%20permission.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/7bc574b8dfa7a952c463e81fd74e57fc58219b9a/00_includes/week%201/assignment%207/executing%20permission.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/7bc574b8dfa7a952c463e81fd74e57fc58219b9a/00_includes/week%201/assignment%207/others&group%20no%20permissions.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/7bc574b8dfa7a952c463e81fd74e57fc58219b9a/00_includes/week%201/assignment%207/permission%20denied.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/7bc574b8dfa7a952c463e81fd74e57fc58219b9a/00_includes/week%201/assignment%207/still%20readable.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/7bc574b8dfa7a952c463e81fd74e57fc58219b9a/00_includes/week%201/assignment%207/group&user%20changed.png)
