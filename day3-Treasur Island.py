#in this section I've learned multiple if statement

print("Welcome to Treasure Island.\nYour mission is to find the treasure")
direction = input("left or right?\n")
swimming = input("swimm or wait?\n")
door = input("which door you wanna get in? red, blue or yellow?\n")

if direction == "left":
    swimming = input("swimm or wait?\n")
    if swimming == "wait":
        door = input("which door you wanna get in? red, blue or yellow?\n")
        if door == "yellow":
            print("you win!!")
        else:
            print("you lost")
    else:
        print("you lost")
else:
    print("you lost")