# breacking Down the problem first
#import pacakge and module

from art import logo, vs
from game_data import data
import random
#first print all game material
print(logo)

choice_one = random.choice(data)
print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']} ")

choice_two = random.choice(data)

if choice_one == choice_two:
    choice_two = random.choice(data)
print(f"Compare B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']} ")





