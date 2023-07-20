# breacking Down the problem first
#import pacakge and module

from art import logo, vs
from game_data import data
import random
#first print all game material
print(logo)
game_continue = True
score = 0
while game_continue:
    print(f"You are right! Current Score {score}")
    choice_one = random.choice(data)
    print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']} ")

    print(vs)
    choice_two = random.choice(data)

    if choice_one == choice_two:
        choice_two = random.choice(data)
    print(f"Compare B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']} ")

    user_choice = input("Who has more follower Type : 'A' or 'B' ").capitalize()

    if choice_one['follower_count']>choice_two['follower_count'] and user_choice=="A":
        score += 1
    elif choice_one['follower_count']<choice_two['follower_count'] and user_choice=="B":
        score += 1
    else:
        game_continue = False
        print(f"Sorry, that is wrong. final score {score}")



