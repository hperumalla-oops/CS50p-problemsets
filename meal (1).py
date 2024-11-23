def one(t):
    a,b=t.split(sep=":")
    a=float(a)
    b=float(b/60)
    t=float(a+b)


def lol(float(t)):
    if t>=7.0 and t<=8.0:
        print("breakfast time")
    elif t>=12.0 and t<=13.0:
        print("lunch time")
    elif t>=18.0 and t<=19.0:
        print("dinner time")

t=input("what time is it?")
one(t)
lol(t)