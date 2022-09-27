# Files & Directories
Learning how to work with directories & files, as well as searching through them.

## Key terminology
Pwd = shows current directory (folder)/ print working directory

Cd = used for navigation between directories and folders

Cd .. = goes 1 directory backwards bv: cd ../

Cd / = open the root directory

Cd /home/ dominic/Techgrounds/ = absolute path to directory Techgrounds

Ls = list of files, shows files within the current directory

Cp = copy files, the commandline cp “insert file you want to copy” “new file name” bv: cp test testcopy

To copy a file to another directory use bv: cp test “path” “/home/dominic”

Rm = remove or delete files bv: rm testcopy only deletes in the directory you are in at the moment

Mkdir= create a new directory/folder bv: mkdir “testfolder” = directory/folder name

Rmdir= delete directory/folder bv: rmdir “testfolder” =selected directory/folder directory needs to be empty in order to be deleted

Rm -r= to delete non empty directories/folders bv: rm -r “testfolder” = directoryname

Clear= to clean up the cmd screen

Man= manual an explanation on a command bv: man ls – shows explanation on the ls command

Cat > “filename.txt” = creates a new file use ctrl+Z to save the .txt file and
exit

Touch “”filename.txt”= creates new file without tekst

Cat “filename.txt”= shows tekst/content of the file

Echo ‘insert text’ > “filename.txt”= allows you to add text/content to the file

Gedit “filename.txt”= opens editor to edit the textfile or leafpad “filename.txt”

## Exercise
### Sources
https://cheatography.com/davechild/cheat-sheets/linux-command-line/

https://www.guru99.com/linux-commands-cheat-sheet.html

https://www.tutorialworks.com/linux-commands/

https://www.youtube.com/watch?v=IVquJh3DXUA&t=268s

https://www.youtube.com/watch?v=N8CMKC-IYPo&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=2

https://www.youtube.com/watch?v=s2bsE7MJTQg&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=3&t=107s

### Overcome challenges
In the links above that show command sheets I found the explanations connfusing and needed something more that showed me why it needs to be filled in to the powershell that way. So I looked through the search machine more specifically like: how to edit text file in Linux. Which showed a few good Youtube video's. In the end I wrote in my notes as shown above in my own words what each command means in order to have a better understanding. This helped me a lot as I needed to search less and less, resulting in finishing this assignment as well.

### Results
I found the directory I was working in with pwd which shows which directory you are currently in. I did need to add a few directories within the home directory as there were none. After that I used ls to view which directories and files were present in the home map. Which showed me Desktop, Pictures, Public and later in the added Techgrounds directory. I created the learn.txt file with the text "Learning to work and use commands in Linux!" which I viewed again with cat learn.txt and I edited it with echo single quot's to let it contain the mentioned text. Also I explored the directories by using the absolute and relative paths to find my way around.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/main/00_includes/current%20directory.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/main/00_includes/home%20directory.png)

![alt text]()
