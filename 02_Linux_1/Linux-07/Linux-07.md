# Bash Scripting
+ Create directory 'scripts' to place all the scripts inside off and set the PATH for the directory. Create scripts that add, execute certain processes.

## Key terminology
Script= a textfile containing a serie of commands you want automate running

Path=complete location of where a file  or anything else could be located at example /users/dominic/documents

Variable= a character to which you assign a value like for example the filename
Httpd= HyperText Transfer Protocol server program and is a standalone daemon/process

Printenv $Path= checks which directories are in the Path

Echo $Path= checks which directories are in the Path

Export PATH=”$HOME/bin: $PATH”= a temporary path fort he current shell session

Nano ~/ .bashrc = to open editor and add the path permanently by typing the export command into the file.

Source ~/ .bashrc= loads the path the directory is in into the current shell session

Echo $PATH= to check if the directory was succesfully added

Nano scripttest.sh= opens the text editor for editing the .sh file which is a shell script 

#! /bin/bash= tells which language you want to use (like code or just the command lines of linux) After this you can add text in the script using echo

Bash scripttest.sh= runs the script by showing the line/string

Writing the command echo like this in nano: echo ‘script testing in progress’ >> learn.txt 

Here we are redirecting the script to the textfile learn.txt each time we use the bash command like above it adds the line we typed into the script file.

apt install apache2= because httpd in windows only uses apache so that is why httpd doesn’t work if entered in the command

Echo $((1 + RANDOM % 10))= a random number between 1 and 10 will be generated
1 is the start of the numbers and with adding random you say it needs to randomly generated, by putting 10 at the end you set the limit of numbers up to 10.

$= add a command substition or variable to execute an expension $time then the variable added is the word “time” you can add the $time variable to any command you make in echo or script

% = modulo

If = Is a condition and you need to close it like this “fi” if [ “$dominic” = dominic ]; then echo “Welcome back dominic” fi, like this if condition will show if the variable is correct that you are welcomed back.

-ge = greater than/or equal to the input given

-lt = lesser than the input given

## Exercise
### Sources
Sources exercise 1:

https://www.tutorialspoint.com/unix_commands/httpd.htm#:~:text=httpd%20is%20the%20Apache%20HyperText,or%20threads%20to%20handle%20requests.

https://medium.com/@ertorrez/use-a-script-to-install-and-launch-an-apache-server-on-centos-8-6db6e4b81cbf

https://www.youtube.com/watch?v=SPwyp2NG-bE

https://linuxize.com/post/how-to-add-directory-to-path-in-linux/

https://www.geeksforgeeks.org/start-stop-restart-services-using-systemctl-in-linux/

Sources exercise 2:

https://www.youtube.com/watch?v=DS0VQAC-gak

https://www.tutorialspoint.com/unix/unix-using-variables.htm#:~:text=A%20variable%20is%20a%20character,%2C%20assign%2C%20and%20delete%20variables.

https://www.youtube.com/watch?v=19nN9vgcgmU

Sources exercise 3:

https://www.youtube.com/watch?v=qoem5hqCH6A

https://www.youtube.com/watch?v=19nN9vgcgmU

https://acloudguru.com/blog/engineering/conditions-in-bash-scripting-if-statements

https://www.youtube.com/watch?v=Ec9WQGw4lW0

### Overcome challenges
Exercise 1:

I was struggling to get the httpd script running I tried executing it using my username and a password which I didn't know. I solved the problem by putting sudo in the command lines so that upon executing the httpd script it would run without question, which it did.

Exercise 2:

The problem was that it wouldn't generate a random number but instead add the line $randomNumber. Later on by removing the quotations it worked and added the random number.

Exercise 3:

The issue was how to make it understand that within the script I meant greater than 5. First I did it mathemattically by using these symbols > <, however these didn't work. 

I should have read the whole page of acloudguru.com as it contained the answer to this question which was to replace the > with -ge. Honestly took me 3 hours before I found out. Because I was just straight up looking for an answer instead of all the information on the side.


### Results
[Describe the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()