

with open('students.csv') as file:
    lines = file.readlines()
    for line in lines:
        values = line.split(',')
        print(values[0], values[2], values[3])
