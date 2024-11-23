import csv

name= input("Enter name ")
house =input("Enter house ")

with open("thingswriter.csv", "a") as notebook:
    note = csv.DictWriter(notebook, fieldnames=["name", "house"])
    note.writerow({"name":'name', "house":'house'})
    note.writerow({"name":name, "house":house})