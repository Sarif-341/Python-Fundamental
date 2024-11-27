print("Welcome to python Pizza Deliveries!!")
size = input("What size pizza do you want? S, M, L: ")
paperoni = input("Do you want peperoni? Y/N:  ")
extra_cheese = input("Do you want extra cheese? Y/N:  ")
size_bill = 0

if size == "S":
    size_bill = 15
    if paperoni == "Y":
        size_bill += 3
    if extra_cheese == "Y":
        size_bill += 1
    print(f"your total bill is ${size_bill}")
elif size == "M":
    size_bill = 18
    if paperoni == "Y":
        size_bill += 3
    if extra_cheese == "Y":
        size_bill += 1
    print(f"your total bill is ${size_bill}")
else:
    size_bill = 20
    if paperoni == "Y":
        size_bill += 3
    if extra_cheese == "Y":
        size_bill += 1
    print(f"your total bill is ${size_bill}")
