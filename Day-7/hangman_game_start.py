import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_letter = input("Guess a letter :  ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# count_char = chosen_word.count(user_letter)

for string in chosen_word:
  if string == user_letter:
    print("Right")
  else:
    print("Wrong")
