import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names[0])

size = len(names)

# print(size)

get_random = random.randint(0 ,size -1)

print(f"{names[get_random]} is going to buy the meal today!")
