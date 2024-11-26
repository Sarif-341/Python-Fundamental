#odd or even number. this section I learned modulo
print("Welcome to Odd or Even Number Generator")
Number = int(input("Please input the Number!! \n"))

if Number % 2 == 0:
    print(f"{Number} is Even Number")
else:
    print(f"{Number} is Odd Number")