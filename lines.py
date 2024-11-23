import sys
import os


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".py"):
        if os.path.isfile(sys.argv[1]):
            new=[]
            with open(sys.argv[1], 'r') as file:
                line=file.readlines()

                for i in range(0,len(line)):
                    x=line[i].lstrip()
                    if x == '':
                        i=i+1
                    elif x.startswith('#'):
                        i=i+1
                    else:
                        #print(x)
                        new.append(x)


                #print(new)
                print(len(new))

        else:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")


