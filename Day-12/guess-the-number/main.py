import random
from art import logo
#Number Guessing Game Objectives:

print(logo)
print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100")
computer_guessing = random.randint(1, 100)
print(computer_guessing)
guess_continue = False
game_level = input("chose a difficult type 'easy' or 'hard' ").lower()
live = 6
if game_level == "hard":
    for count in range(5):
        while not guess_continue:
            user_guess = int(input("Make a Guess "))
            if computer_guessing == user_guess:
                print(
                    f"The Computer Guss {computer_guessing} and You Guss {user_guess} so You are Correct"
                )
                guess_continue = True
            else:
              live -= 1
              print(f"You attempt {live} remain to Guess the Number")
              if user_guess > computer_guessing:
                print("To High")
                print("Guess Agin")
              else:
                print("To Low")
                print("Guess Agin")
              if live == 1:
                    guess_continue = True
live = 10
if game_level == "easy":
    for count in range(5):
        while not guess_continue:
            user_guess = int(input("Make a Guess "))
            if computer_guessing == user_guess:
                print(
                    f"The Computer Guss {computer_guessing} and You Guss {user_guess} so You are Correct"
                )
                guess_continue = True
            else:
              live -= 1
              print(f"You attempt {live} remain to Guess the Number")
              if user_guess > computer_guessing:
                print("To High")
                print("Guess Agin")
              else:
                print("To Low")
                print("Guess Agin")
              if live == 1:
                    guess_continue = True
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
