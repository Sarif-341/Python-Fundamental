#in this section I've learned nested mulriple if statement.
#ticket programed for someone with height >= 120cm and age over 18 years old and ask them if they want a foto

print ("welcome to Rollercoaster")
height = int(input("input your height \n"))
bill = 0

if height >= 120:
    print("Hello, you can ride our rollercoaster")
    age = int(input("input your age \n"))
    if age < 12:
        bill = 5
    elif age > 18:
        bill = 12
    else:
        bill = 7

    photo = input("do you want photo? y/n \n")
    if photo == "y":
        print(f"your total bil is ${bill + 3}")
    else:
        print(f"your bill is ${bill}")
else:
    print("you can't ride")
