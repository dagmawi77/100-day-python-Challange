from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program. ")

other_user = False
# new_bider_dictinary = {}
bider_dictinary = {}


def higest_bider(bedding_record):
  highest = 0
  winner = ""
  for bidder in bedding_record:
    bidder_amount = bedding_record[bidder]
    if bidder_amount > highest:
      highest = bidder_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest}")


while not other_user:
  name = input("What is your name?:")
  bid = int(input("What's your bid?: $"))
  bider_dictinary[name] = bid
  other_bider = input("Are there any other bidders? Type 'yes' or 'no'.yes")
  if other_bider == "no":
    other_user = True
    higest_bider(bider_dictinary)
  elif other_bider == "yes":
    clear()
  # new_bider_dictinary =bider_dictinary

# print(new_bider_dictinary)
