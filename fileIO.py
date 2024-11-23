import csv

students =[]
with open("things1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row['name'], "home": row['home']})

for student in students:
    print(f"{student['name']} lives in{student['home']}")