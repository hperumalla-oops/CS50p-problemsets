due=50
print("Amount Due:",due)
x=int(input("Insert Coin: "))
while x==50 or x==25 or x==10 or x==5:
        if x<due:
            due=due-x
            print(f"Amount Due:",due)
            x=int(input("Insert Coin: "))
            continue
        else:
            print("Change Owed:",x-due)
        break
else:
     print("Amount Due:",due)
