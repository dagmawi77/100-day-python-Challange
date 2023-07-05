import random
#from art import logo
#Number Guessing Game Objectives:

#print(logo)
print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100")
computer_guessing = random.randint(1, 100)
print(computer_guessing)
game_level = input("chose a difficult type 'easy' or 'hard' ").lower()
if game_level == "easy":
  guess_continue = False
  user_guess = int(input("Make a Guess"))
  for _ in range(5):
    while not guess_continue:
      if computer_guessing == user_guess:
        print(
          f"The Computer Guss {computer_guessing} and You Guss {user_guess} so You are Correct"
        )
        guess_continue = True
      else:
        print(f"You attempt is {_}")
    guess_continue = False
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
