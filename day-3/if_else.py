print("The Rule For Air port Employeement")

hight = float(input("Input Your Hight with cm  "))

if hight >= 1.70:
  print("You can Work with Us")
  age = int(input("How Old Are You ? "))
  if age >= 30:
    print("You pass your hight but you so old")
  elif age >= 50:
    print("I think you need pention")
  else:
    print("Sucussfuly Hired Welcome to Airlines")
else:
  print("we don't place for you ")
