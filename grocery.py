str_list = []
count=0
items=[]
final_count=[]


try:
    while True:
        str_list.append(str(input()).upper())

except EOFError:

        for n in range(len(str_list)):
            if str_list[n] in items:
                n=n+1

            else:
                for i in range(len(str_list)):
                    if str_list[n] == str_list[i]:
                        count=count+1

                else:

                    items.append(str_list[n])
                    n=n+1

                    final_count.append(count)
                    count=0





for _ in range(len(items)):
    print(final_count[_],items[_])

