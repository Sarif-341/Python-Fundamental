print("Welcome to python Pizza Deliveries!!")
size = input("What size pizza do you want? S, M, L: ")
paperoni = input("Do you want peperoni? Y/N:  ")
extra_cheese = input("Do you want extra cheese? Y/N:  ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 18
elif size == "L":
    bill = 20
else:
    print("Your input is false, please try again!!")

if paperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill} ")