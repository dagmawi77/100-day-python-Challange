# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

bmi = float(weight) / float(height)**2

print(round(bmi))

#Write your code below this line 👇

print(
  f"You hight is {height} and your weight is {weight} and you BMI is {bmi}")
