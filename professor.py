import random
def main():

        x=get_level()
        s=0
        for i in range(10):

            lol = generate_integer(x)
            int1=lol[0]
            int2=lol[1]
            sum=lol[2]
            s=Range(s,sum,int1,int2)

            i=i+1

        print("Score:",(10-s))



def get_level():
        while True:
            level=input("Level: ")
            try:
                level=int(level)
            except ValueError:
                continue
            else:
                if level>=1 and level<=3:
                    return int(level)
                else:
                    continue

def generate_integer(level):
        if level==1:
            a=random.randint(0,9)
            b=random.randint(0,9)

        elif level==2:
            a=random.randint(10,99)
            b=random.randint(10,99)

        elif level==3:
            a=random.randint(100,999)
            b=random.randint(100,999)

        c=a+b
        lol=[a,b,c]
        return lol

def Range(s,sum,int1,int2):
            for i in range (3):
                    r=input(f"{int1} + {int2} = ")
                    try:
                        r= int(r)
                    except ValueError:
                        print("EEE")
                        i=i+1
                    else:
                        if r != sum:
                            print("EEE")
                            i=i+1
                        else:
                            break

            if i==3:
                s=s+1
                #print(s)
                print(f"{int1} + {int2} = {sum}")

            return s

if __name__ =="__main__":
    main()

