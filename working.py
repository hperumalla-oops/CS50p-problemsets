import re

def main():
    #for i in range(0,8):
         print(convert(input("Hours: ")))

def convert(s):
    try:
        x=s.split("to")
        x[0],x[1]
    except IndexError:
        raise ValueError
    else:
        for i in range(0,2):
            x[i]=x[i].lstrip()

        if "AM" in x[0]:
            if morning(x[0]) ==2 or night(x[1])==2:
                #print("fart")
                raise ValueError
                #return "ValueError"

            return f"{morning(x[0])} to {night(x[1])}"
        else:
            if morning(x[1]) ==2 or night(x[0])==2:
                #print("fart")
                raise ValueError
                #return "ValueError"

            return f"{night(x[0])} to {morning(x[1])}"



def morning(i):

    if bool(re.match(r'([0-9][2]:[0-5][0-9] [A][M])',i)):
        m="00:00"

    elif bool(re.match(r'([1][2] [A][M])',i)):
        m="00:00"

    elif (bool(re.match(r'([1-9] [A][M])',i))):
        i=int(i.replace("AM",""))
        m="0"+str(i)+":"+"00"

    elif bool((re.search(r'([1-9]:[0-5][0-9] [A][M])', i))):
        i=i.replace("AM","")
        m="0"+i
        m=m.rstrip()

    else:
        return 2


    return m

def night(i):
    #i=i.lstrip()
    #print(i)
    if bool(re.match(r'([1][2]:[0-5][0-9] [P][M])',i)):
        n="12:00"

    elif bool(re.match(r'([1][2] [P][M])',i)):
        n="12:00"

    elif bool((re.search(r'([1-9]:[0-5][0-9] [P][M])', i))):
        i=i.replace("PM","")
        l=i.split(":")
        l[0]=int(l[0])+12
        n=str(l[0])+":"+l[1]
        n=n.rstrip()

    elif bool(re.match(r'([1-9] [P][M])',i)):
        i=int(i.replace("PM",""))+12
        n=str(i)+":"+"00"

    else:
        return 2

    #print("night tiem is",len(n))
    return n


if __name__ == "__main__":
    main()


