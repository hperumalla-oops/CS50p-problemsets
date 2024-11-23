import sys
import csv
import os

first1=[]
last1=[]
house1=[]
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if os.path.isfile(sys.argv[1]):

            with open(sys.argv[1], "r") as lol:
                notebook = csv.DictReader(lol)
                for line in notebook:
                    try:
                        last, first = line['name'].split(", ")
                    except ValueError:
                        pass

                    house=line['house']


                    first1.append(first)
                    last1.append(last)
                    house1.append(house)

            with open(sys.argv[2], "w", newline='') as file:
                file.write("first,second,house\n")
                for _ in range(len(first1)):
                    note =csv.DictWriter(file, fieldnames =["first", "last", "house"])
                    note.writerow({"first": first1[_] ,"last":last1[_], "house":house1[_]})

    else:
        sys.exit("Could not read " + sys.argv[1])
