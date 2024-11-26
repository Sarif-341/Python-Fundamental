#in this section I've learned nested mulriple if statement.
#ticket programed for someone with height >= 120cm and age over 18 years old

print ("welcome to Rollercoaster")
height = int(input("input your height \n"))

if height >= 120:
    print("Hello, you can ride our rollercoaster")
    age = int(input("input your age \n"))
    if age < 12:
        print("you should pay $5")
    elif age > 18:
        print("you should pay $12")
    else:
        print("you should pay $7")
else:
    print("you can't ride")
