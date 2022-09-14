import csv

with open('students.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row[0], row[2], row[3])
        