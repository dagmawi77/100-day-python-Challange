#String manipulation

# it all About String manipulation On python
# the first  Step is String Conactination It all about Combine Two Or more String on one here is the exampel

str1 = "Hello"
str2 = "Python"
# the Plus Sign is help To Concatinate the string
result = str1 + " " + str2

print(result)

# the Second mainpulation Methood is slicing it about get some of the portion from the declared String

myString = "Hello World"
# any programing is Counting From 0 so you get Hello Wold only by below command
print(myString[0:5])

print(myString[6:])
# It print the reverse String based on Sliced postion
print(myString[:5:-1])

# the Thired String Manipulation is replacing it help to Modifed the String by Replacing Spacific Word

myStringOne = "Hello World"
newString = myStringOne.replace("World", "Python3")
print(newString)

# The Forth One is String Formating this is Hlep to Get Daynamic String

fname = input("Can You Enter Your First Name ? \n")
age = input("Can You Enter You Age \n")

ageConverter = str(age)

# There are 3 Type of String Formating % mode str.format and f-string Mode

#The % mode Example
message = "The User name is %s and the Age is %s" % (fname, ageConverter)
print(message)

name = "Alice"
age = 25
message = "My name is %s and I am %d years old." % (name, age)
print(message)  # Output: My name is Alice and I am 25 years old.

#The str.format method

messageTwo = "The User Name is {} and his Age is {}".format(name, age)
print(messageTwo)

#The f-string Method

messageThree = f"The User Name is {name} and his Age is also {age}"

print(messageThree)
