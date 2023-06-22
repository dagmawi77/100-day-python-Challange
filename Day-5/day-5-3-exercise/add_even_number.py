#Write your code below this row 👇
sumOfEven = 0
for number in range(1, 101):
    if number % 2 == 0:
        sumOfEven += number
        # print(number)
print(f"The Sum Of Even number is {sumOfEven}")

# solution Two
sumOfEven = 0
for number in range(0, 101, 2):
    sumOfEven += number
    # print(number)
print(f"The Sum Of Even number is {sumOfEven}")