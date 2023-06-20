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

user_choies = int(
  input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
game_image = [rock, paper, scissors]
if user_choies >= 3 or user_choies < 0:
  print("You Enter Invalid Number For the Game")
else:

  print(f"User Choices Is... {game_image[user_choies]}")
  computer_choies = random.randint(0, 2)
  print(f"Computer Choice Is ... {game_image[computer_choies]}")
# Rock wins against scissors
# paper wins against rock
# scissors wins against paper.
if (user_choies == 0 and computer_choies == 2) or (
    user_choies == 1 and computer_choies == 0) or (user_choies == 2
                                                   and computer_choies == 1):
  print("The User is Win This Game")
elif (computer_choies == 0 and user_choies == 2) or (
    computer_choies == 1 and user_choies == 0) or (computer_choies == 2
                                                   and user_choies == 1):
  print("The Computer Win This Game")
else:
  print("The Game End With Draw")
