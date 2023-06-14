# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇age
ageInt = int(age)

constInt = 90

remainAge = constInt - ageInt

day = remainAge * 366

week = day / 7

month = day / 30

print(f"You Have {day} Day , {week} Week and {month} remain ")
