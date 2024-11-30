import random

game = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

player = int(input("what do you choose? type 0 for paper, 1 for rock, 2 for scissor\n"))
if player > 2 :
    print("invalid number")
else:
    print(f"you've chose: {game[player]}")

computer = random.randint(0, 2)
print(f"computer chose {game[computer]}")

if player > 2:
    print("you lose!!")
elif computer == 0 and player == 2:
    print("computer win")
elif player == computer:
    print("draw")
elif player > computer:
    print("you win")
else:
    print("computer win")
