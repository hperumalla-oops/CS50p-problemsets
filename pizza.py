from tabulate import tabulate
import sys
import os
def list(lines):
            new=[]
        #for i in range(1,len(lines)):
            a,b,c= lines.split(',')
            c=c.replace('\n','')
            new.append(a)
            new.append(b)
            new.append(c)

            return new

new2=[]
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".csv"):
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1]) as file:
                lines=file.readlines()
                a,b,c= lines[0].split(',')
                c=c.replace('\n','')
                for i in range(1,len(lines)):
                    new2.append(list(lines[i]))


            #print("finally",new2)
            table = new2

            headers = [a,b,c]
            print(tabulate(table, headers, tablefmt="grid"))


        else:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")

