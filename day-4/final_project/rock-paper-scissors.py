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

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
))
user_list=[rock,paper,scissors]
print(f"user choice is ..{user_list[user_choice]}")
computer_list =[rock,paper,scissors]
computer_choice = random.randint(0,2)
print(f"Computer Choice is ....{computer_list[computer_choice]}")
# Rock wins against scissors; 
# paper wins against rock; 
# scissors wins against paper
if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0 ) or (user_choice == 2 and computer_choice == 1 ):
  print("You Win The Game")
elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0 ) or (computer_choice == 2 and user_choice == 1 ):
  print("You Lost The Game")
else:
  print("Both Draw The Game")