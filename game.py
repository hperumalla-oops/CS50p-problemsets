import random

def VE():
    while True:
        try:
            z = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if x<=0:
               continue
            else:
                return z


def VL():
    while True:
        try:
            x = int(input("Level: "))
        except ValueError:
            pass
        else:
            if x<=0:
               continue
            else:
                return x

x=VL()
#print("from the range 1-",x,sep="")

y=random.randint(1,x)
#print("random integer is ",y)

z=VE()
while z!=y:
    if z<y:
            #print(z,"<",y)
            print("Too small!")
            z=VE()
    else:
            #print(z,">",y)
            print("Too large!")
            z=VE()

else:
     #print(z,"=",y)
     print("Just right!")
