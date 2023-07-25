# breacking Down the problem first
#import pacakge and module

from art import logo, vs
from game_data import data
import random
<<<<<<< HEAD
# import replit
#first print all game material
print(logo)


game_continue = True
score = 0
while game_continue:

=======
from replit import clear
#first print all game material
print(logo)
game_continue = True
score = 0
while game_continue:
>>>>>>> e981c422ac5c53cc7422b3f3b3675effa28c3ff1
    choice_one = random.choice(data)
    choice_two = random.choice(data)
    if choice_one == choice_two:
        choice_two = random.choice(data)
<<<<<<< HEAD
    print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']} ")
    print(vs)
    print(f"Compare B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']} ")
    user_choice = input("Who has more follower 'A' or 'B' ").capitalize()
    if choice_one['follower_count'] > choice_two['follower_count'] and user_choice == "A":
        score += 1
        print(f"Your right current score {score}")
    elif choice_one['follower_count'] < choice_two['follower_count'] and user_choice == "B":
        score += 1
        print(f"Your right current score {score}")
    else:
        print(f"Sorry, that is wrong. Final Score {score} ")
        game_continue = False
        
=======
    print(
        f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']} "
    )
    print(vs)
    print(
        f"Compare B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']} "
    )
    user_choice = input(
        "Who has more follower Type : 'A' or 'B' ").capitalize()
    clear()
    print(logo)
    if choice_one['follower_count'] > choice_two[
            'follower_count'] and user_choice == "A":
        score += 1
        print(f"You're right! Current score: {score}.")
    elif choice_one['follower_count'] < choice_two[
            'follower_count'] and user_choice == "B":
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry, that is wrong. final score {score}")
>>>>>>> e981c422ac5c53cc7422b3f3b3675effa28c3ff1
