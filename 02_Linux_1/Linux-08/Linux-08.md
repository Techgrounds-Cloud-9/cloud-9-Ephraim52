# Cron Jobs
Create script to automate writing the current time, date & available disk space to specified files named in the exercise.

## Key terminology
Cron = a job scheduling utility if you use specific syntax you can configure a cron job to schedule commands to run automatically

Df = a command to see the disk space available

(-)H = shows the amount of bytes listed by 1000. For example 1000B = 1kb = 1 kilobyte

(*) = any value can be filled in here for example 0 – 9 

` = not a quotation, but anything you typ between the backtick will be evaluated and executed by the shell


## Exercise
- Create a Bash script that writes the current date and time to a file in your home directory.
- Register the script in your crontab so that it runs every minute.
- Create a script that writes available disk space to a log file in '/var/logs'. Use cron job so that it runs weekly.

### Sources
https://www.cyberciti.biz/tips/shell-script-to-watch-the-disk-space.html

https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

https://www.howtogeek.com/409611/how-to-view-free-disk-space-and-disk-usage-from-the-linux-terminal/#:~:text=Bash%20contains%20two%20useful%20commands,terminal%20window%20to%20get%20started

https://unix.stackexchange.com/questions/27428/what-does-backquote-backtick-mean-in-commands

https://crontab.guru/#0_0_*_*_1

https://www.freecodecamp.org/news/cron-jobs-in-linux/#:~:text=Cron%20is%20a%20job%20scheduling,other%20commands%20to%20run%20automatically.

The presentation about Cron jobs helped me. I would like to mention that and thank them for that.

### Overcome challenges
One of the challenges I had was to figure out why it wouldn't execute the script in which I typed the command: today='date'. It wouldn't execute the date command because quotations don't do executions of commands. 

So I looked up what did execute commands in this manner and found out that the backquote/backtick `` does this.

### Results
[Describe the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]
![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()

![alt text]()
