import sys
str_list = []

dict ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

food = [
    "BAJA TACO",
    "BURRITO",
    "BOWL",
    "NACHOS",
    "QUESADILLA",
    "SUPER BURRITO",
    "SUPER QUESADILLA",
    "TACO",
    "TORTILLA SALAD",
]

# print(food[0])
r=0
cost = [4.2501, 7.501, 8.501, 11.00, 8.501, 8.501, 9.501, 3.00, 8.00]
while True:
    try:
        #while True:
            x = input("Item: ").upper()
            if x in food:
                for i in range(len(cost)):
                    if x == food[i]:
                        r=r+cost[i]
                        r=round(r,2)
                        #str_list.append(food[i])
                        #formatted_number = f"{number:.2f}"
                        print(f"${r:.2f}")

                        pass
                    else:
                        i=i+1
                        #total = total + cost[i]
            else:
                pass
    except EOFError:

        sys.exit()