#Write your code below this row 👇
fizzBuzz = ""
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    fizzBuzz = "FizzBuzz"
    print(fizzBuzz)
  elif number % 3 == 0:
    fizzBuzz = "Fizz"
    print(fizzBuzz)
  elif number % 5 == 0:
    fizzBuzz = "Buzz"
    print(fizzBuzz)
  else:
    fizzBuzz = number
    print(fizzBuzz)
