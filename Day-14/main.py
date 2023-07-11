# The first step adding random package
import random
from art import logo, vs
from game_data import data

# printing basic interface
print(logo)
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

continue_game = True
while continue_game:

  user_guess = input("Who has More Follower? Type 'A' or B ").capitalize()

  if choise_a['follower_count'] > choise_b[
      'follower_count'] and user_guess == "A":
    print("User win")
  elif choise_b['follower_count'] > choise_a[
      'follower_count'] and user_guess == "B":
    print("User win")
  else:
    print("user lost")
    continue_game = False
