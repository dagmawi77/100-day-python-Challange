#Write your code below this line 👇
def prime_checker(number):
  prime_number = True
  for i in range(2, number):
    if number % i == 0:
      prime_number = False
  if prime_number:
    print(f"{number} is Prime number")
  else:
    print(f"{number} is not prime number")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
