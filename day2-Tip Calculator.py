#in this project I will create tip calculator
#in this section I've learned about data types including float, integer, string and boolean
#bonus section I learned python built-in function called round
print("welcome to tip calculator")
BIll = float(input("what was the total bill? $"))
Tip = int(input("how much tip would you like to give? 10, 12, or 15? $"))
Split = int(input("how many people to split the bill?"))
print(f"Each person should pay: ${round((BIll+Tip)/Split, 2)}" )
