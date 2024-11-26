print("Welcome to python Pizza Deliveries!!")
size = input("What size pizza do you want? S, M, L: ")
paperoni = input("Do you want peperoni? Y/N:  ")
extra_cheese = input("Do you want extra cheese? Y/N:  ")
size_bill = 0
peperoni_price = 3
cheese_price = 1

if size == "S":
    bill = 15
    if paperoni == "Y":
        size_bill += 3

elif size == "M":
    bill = 18
else:
    bill = 20

