net_runs=[]
x=int(input())
for _ in range(x):
    net_runs.append(input())

print(net_runs)
for k in range(len(net_runs)):
    list1=[]
    list1=net_runs[k].split()
    print(list1)
    for i in range(0,4):
        if list1[i]=="W" and list1[i+1] == "W" and list1[i+2] == "W":
                    print("YES")

    print("NO")


