# The first step adding random package
import random
from art import logo, vs
from game_data import data

from replit import clear

# printing basic interface
print(logo)

life = 0
continue_game = True
while continue_game:
  choise_a = random.choice(data)

  print(
    f"Compare A: {choise_a['name']} a {choise_a['description']} , from {choise_a['country']}"
  )

  print({choise_a['follower_count']})

  print(vs)

  choise_b = random.choice(data)
  print(
    f"Compare B: {choise_b['name']} a {choise_b['description']} , from {choise_b['country']}"
  )
  print({choise_b['follower_count']})

  user_guess = input("Who has More Follower? Type 'A' or B   ").capitalize()

  if choise_a['follower_count'] > choise_b[
      'follower_count'] and user_guess == "A":
    life += 1
    print(f"your right current score {life}")
  elif choise_b['follower_count'] > choise_a[
      'follower_count'] and user_guess == "B":
    life += 1
    print(f"your right current score {life}")
  else:
    continue_game = False
    print(f"sorry , that is wrong.Final Score: {life}")
    clear()
