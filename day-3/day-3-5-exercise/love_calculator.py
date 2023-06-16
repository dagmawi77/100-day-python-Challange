# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conv_name1 = name1.lower()
conv_name2 = name2.lower()
combined_string = conv_name1 + conv_name2
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v + e
true_love_str = str(true) + str(love)

true_love_int = int(true_love_str)

if true_love_int > 90 or true_love_int < 10:
  print(
    f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int >= 40 and true_love_int <= 50:
  print(f"Your score is {true_love_int}, you are alright together.")
else:
  print(f"Your score is {true_love_int}.")
