def mul_table():
    x=int(input("Enter the multiplication table of the number you require\n"))
    y=1
    for y in range(1,21):
        print(f"{n}X{y}={x*y}\n")
        y=y+1

mul_table()