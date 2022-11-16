# Key-value pairs
How key-values work and how the dictionary comes into play here.

## Key terminology
Dictionaries= Are used to store data values in key:value pairs. It is a collection which is ordered and changable, written with curly brackets {}.

CSV= comma-seperated values, a file which can read/write or just append(add) information to. 

## Exercise
- Create a new script.
- Use user input to ask for their information (first name, last name, job title, company). Store the information in a dictionary.
- Write the information to a csv file (comma-separated values). The data should not be overwritten when you run the script multiple times.

### Sources
https://www.w3schools.com/python/python_dictionaries.asp

https://www.quora.com/How-can-I-make-the-user-input-key-and-value-dictionary-in-Python-e-g-classe_list-input-name-score-wrong-syntax

https://www.youtube.com/watch?v=q5uM4VKywbA

https://www.pythontutorial.net/python-basics/python-write-csv-file/

### Overcome challenges
I had to find a way to put the dictionary in as it looked simular to how HTML and CSS work together. I found the explanations on python and file handling (csv) confusing as certain explanations felt contradictory to what was meant by this assignment. Eventually with some help from my team mates I realized I needed to put my variables with the input at the top so the variable could be linked to the dictionary. After which I could write the csv file, which VSC printed in a different location then it should have. But even this we solved by just taking the code/python folder seperately at that point it made the file in the same folder.

### Results
This is the python code where the csv file is imported to be used as a data base for saving the input information.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/b90802d38cb109bf61677fc18bb2e690957de629/00_includes/week%204/assignment%208/PRG-08_exercise8p2_py_code.png)

Csv file with the input from the terminal.

![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-Ephraim52/blob/b90802d38cb109bf61677fc18bb2e690957de629/00_includes/week%204/assignment%208/PRG-08_exercise8p2_csv.png)

You need to import this file into the python file, import csv, then write the variables along with the user input question. You connect the variable of the user input with the header list in the dictionary which I gave the variable 'row'. I opened the csv file to append the user input, by giving it the writers commands to write the key-value pairs into the file and save it by closing. I used "with" you can also do it seperately by using "open" "closed", the "with" function does both so I didn't need to close it seperately. 
