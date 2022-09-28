# Working with text (CLI)
redirecting output to other files

## Key terminology
Pipe - "|" this symbol is the pipe can be used for the input or output of a command

Less /home/dominic (path)= shows through the path what the content of the file is that it is directed to

Grep allow you to search and filter as example: cat filename.txt | grep filename this case it shows the line/sentence where the word filename is indicated

Cat filename.txt | grep filename > test.txt t oredirect the output of filename.txt to test.txt (also creates the new file test.txt)

Echo ‘insert text’ > “filename.txt”= allows you to add text/content to the file after the redirection you can also insert a new filename to create another .txt

Echo ‘insert text’ >> “filename.txt”= allows you to add another line through using double >> 

## Exercise
### Sources
https://www.youtube.com/watch?v=cCw5Kb1YnFE

https://www.youtube.com/watch?v=CaJYuRgRQxg&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=5

https://www.youtube.com/watch?v=s2bsE7MJTQg&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=3

https://www.youtube.com/watch?v=nLa6jAbULe8&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=7

Also a mention that previous assignments what I learned there helped me out with which commands were needed for the assignment. Commands I already knew a few off.

### Overcome challenges
Making only the output of "techgrounds" appear I searched which other commands were needed aside of cat to view the file to single out the sentence containing techgrounds. For which I used the grep command which allowed me to single out the techgrounds output. 

The other issue I encountered was redirecting this output to a new file that needed to be created called "techgrounds.txt" I learned that aside of grep I needed to redirect this output to the new file using ">" this symbol means directing towards a file or directory. In the end the file was made with the desired output. 

All I have been doing to solve these issues was search as specifically as possible for the commands and how they are connected to eachother. Learning this how they work to eachother allowed me to solve the issues I spoke off.

### Results
The exercise taught me better on how to search more specifically which yielded better search results. As well ass how the commands work to eachother this allowed me to combine commands in a single line to produce the exercise.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/d329f2cb7b1217642c0d61ee6fabcb567e9fef8c/00_includes/week%201/assignment%205/edited%20lines.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/d329f2cb7b1217642c0d61ee6fabcb567e9fef8c/00_includes/week%201/assignment%205/only%20techgrounds.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/d329f2cb7b1217642c0d61ee6fabcb567e9fef8c/00_includes/week%201/assignment%205/redirecting%20output.png)

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/d329f2cb7b1217642c0d61ee6fabcb567e9fef8c/00_includes/week%201/assignment%205/textfile%20made.png)
