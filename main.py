import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print(rock)
print(paper)
print(scissors)

print("Welcome To Rock Paper & Scissors Game!!!!\n")

name = input("What is Your Name???\n")

user_choice = int(input("Dear " + name + " What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
if user_choice >=3 or user_choice < 0:
  print("Dear " + name + " You typed an invalid number!!! You Lose!!! 3:-)")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Dear " + name + " Computer Choose:")
  print(game_images[computer_choice])


  if user_choice == 0 and computer_choice == 2:
    print("Dear " + name + " You Win!!!!!")
  elif computer_choice == 0 and user_choice == 2:
    print("Dear " + name + " You Lose!!!!!")
  elif computer_choice > user_choice:
    print("Dear " + name + " You Lose!!!!!")
  elif user_choice > computer_choice:
    print("Dear " + name + " You Win!!!!!!")
  elif computer_choice == user_choice:
    print("Dear " + name + " It's a draw")

    print("\n)")

    print("--------------------------------------------------------")
