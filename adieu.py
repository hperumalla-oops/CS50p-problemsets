
str_list = []

name=input("Name: ")
str_list.append(name)

try:
    while name != "":
        name=input("Name: ")
        str_list.append(name)

except EOFError:

    x=len(str_list)
    n=0

    if x==1:
        print("\n","Adieu, adieu, to ",str_list[0],sep="")
    elif x==2:
        printing_string ="Adieu, adieu, to "
        printing_string = printing_string + str_list [0] + " and " + str_list[x-1]
        print(printing_string)


    else :
        printing_string ="Adieu, adieu, to "

        try :
            while str_list[n] != "" and n < (x-1):
                    printing_string = printing_string + str_list[n] +", "
                    n=n+1

            else:
                printing_string = printing_string + "and " + str_list[x-1]
                print("\n",printing_string,sep="")

        except EOFError:

            printing_string = printing_string + "and " + str_list[x-2]
            print(f"\n")
            print(printing_string)

