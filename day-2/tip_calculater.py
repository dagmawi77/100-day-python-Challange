#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_persentage = float(
  input("How much tip would you like to give? 10, 12, or 15? "))
tip_convert = (tip_persentage / 100) * total_bill
total_fee = total_bill + tip_convert
split_person = input("How many people to split the bill? ")
split_person_int = int(split_person)

result = (total_fee / split_person_int)
final_amount = "{:.2f}".format(result)

print(f"Each person should pay: {final_amount}")
