# recup all last day Concepts
# first about how can we print any statment

print("Print Any Statment")

# how can we Concatinate the Strings in print

print("Adding Two Statments like" + "......" + "This")

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

# About Variable  is like phonebook that is about reference or Additional name of the Existing

variableName = "Holding This Message"

print(variableName)

# variable Naming we can give the name of Variable Strting with letter or _
variable_Name = "This Is Valid Variable"
_Var = "This Is also Valid Valiable"
var_1 = "This Alos other Valid Varibale"
# 5642FGSFGS="gsdgdsja" this Kind of Variable
# %$62="This is also Not valid Variable"

# About Data Type is means The the Variable that hold what kind of Data type like integer,String and Boool and Float

# Python is Dynamicly typed languge It means You can't Defined the data type before variable name it automaicaly know the type

# String Data Type

strType = "This Is String Data Type"

print(type(strType))

#integer Data Type

intType = 1001

print(type(intType))

# float Data Type

floatType = 345.22

print(type(floatType))

# Bool data Type

boolType = True

print(type(boolType))

# Type Convertion converting int to String

intType1 = 355
strConv = str(intType1)
print(type(strConv))

# Converting String To int

strType1 = "300"
intConv = int(strType1)

print(type(intConv))
print(intConv)

# You can Convert Any Type Of data if it is possible

#The Variable Callenge It take 2 number and swap the value

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))

numOne = int(two_digit_number[0])
numTwo = int(two_digit_number[1])

print(numOne + numTwo)

# About Matimatical Operation

# addition

print(22 + 33)

# Subtraction

print(33 - 22)

# Multiplication
print(50 * 4)

# devision

print(50 / 4)

#Exponintal

print(4**3)

# Other Type is Complex Number

complex_num = 2 + 3j

print(complex_num.real)
print(complex_num.imag)

#It all About Additional Data type like list,tuple,dictionary,set,frozenset
name = "Hello You"

print(len(name))

# Example Of List
numbers = [10, 22, 44, 66]

print(numbers)
print(numbers[2])

# Example Of Tuples

weekdays = ("Monday", "Tusday", "Wednsday", "Thrsday", "Friday")

print(weekdays)
print(weekdays[2])

# Dictionary

student_info = {"name": "Dagmawi Letarik", "age": 27, "Countery": "Ethiopia"}
print(student_info)

print(student_info["name"])
# Set

furutSet = {"banana", "oragnge"}
furutSet.add("apple")
print(furutSet)

# frozenset

vowels = frozenset("aeiou")
print(vowels)

# None Type

noneType = None
print(noneType)
