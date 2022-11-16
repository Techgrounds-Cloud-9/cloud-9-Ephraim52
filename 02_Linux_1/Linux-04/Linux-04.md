# Users and Groups
Create a new user give sudo permission add to group(s) and set a password.

## Key terminology
Cat /etc/passwd= shows the usergroup

Useradd “enter username”= creates a new user

Id = shows user id group(s)

Passwd welcome= allows you to add/change password for the user welcome

Password will not appear and the cursor won’t move either this is ok it takes the input while being private.

Group id: welcome: x : 1001 : 1001 : : /home/welcome/bin/sh
1001 group ID between the double : : you can add your name 

Cat /etc/group = shows the groups with the ID’s

Useradd -G superheros ironman = adds a new user tot he existing group G respresenting a group

Usermod -G superheros ironman = add existing user to the group also -g like this is primary group and -G is secondary and anything beyond that


## Exercise
### Sources
https://www.youtube.com/watch?v=Nr4GWbGGtz0

https://www.youtube.com/watch?v=s23NqWKxOXk&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=9&t=426s

https://www.youtube.com/watch?v=-OzmiIPOTxI&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=10

https://www.youtube.com/watch?v=iXUHWtgzPMY&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=11&t=606s

### Overcome challenges
I had to look into how to add a newly created user to a group and to add it to multiple groups. Which I used these videos for and also to check if the new user was able to use sudo rights. Just by patiently listening I understood how the commandlines worked and were structured to do specific things like adding to multiple groups, set primary or a secundary group.

### Results
The result is as shown in the multiple screenshots, where you can see that I added the new user "welcome" to the groups sudo and admin. As well as showing that I could find the info in the files group and passwd. In the end a final check to see if the user was able to use sudo rights.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/75db32c695f2acbff7bfdde1383a6f207ca1faed/00_includes/week%201/assignment%206/new%20user%20welcome.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/75db32c695f2acbff7bfdde1383a6f207ca1faed/00_includes/week%201/assignment%206/shows%20groups.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/75db32c695f2acbff7bfdde1383a6f207ca1faed/00_includes/week%201/assignment%206/shows%20sudo%20priv.png)

!![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/75db32c695f2acbff7bfdde1383a6f207ca1faed/00_includes/week%201/assignment%206/shows%20uid,%20gid.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/75db32c695f2acbff7bfdde1383a6f207ca1faed/00_includes/week%201/assignment%206/sudo%20priveliges.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/75db32c695f2acbff7bfdde1383a6f207ca1faed/00_includes/week%201/assignment%206/welcome%20password.png)
