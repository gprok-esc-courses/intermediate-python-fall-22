import csv

with open('students.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row['SIS ID'], row['First Name'], row['Last Name'])

