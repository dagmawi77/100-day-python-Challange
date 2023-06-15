print("Do You want To play The Game? ")
hight = float(input("What is Your Hight in CM? "))

if hight >= 1.60:
  age = int(input("please insert your age .."))
  if age < 12:
    bill = 15
    print(f"You are child so you Pay ${bill}")
  elif age < 19:
    bill = 20
    print(f"You are Young so you Pay ${bill}")
  else:
    bill = 25
    print(f"You are Adult so you Pay ${bill}")
  want_photo = input("Do You want Photo say 'Y' or 'N' ")
  if want_photo=="Y":
    bill+=3
print(f"Your Total Bills is {bill}")
else:
  print("You Can't Play this game Becaue You are short")
