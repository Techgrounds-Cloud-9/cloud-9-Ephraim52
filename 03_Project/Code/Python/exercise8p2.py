import csv

firstname = input("What is your first name?")
lastname = input("What is your last name?")
jobfunction = input("What is your current or previous job function?")
company = input("At which company did you work or used to work for?")

row= {
    'first name' : firstname, 
    'last name' : lastname,
    'job function' : jobfunction,
    'company' : company
}

with open('personalinfo.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(row.keys())
    writer.writerow(row.values())