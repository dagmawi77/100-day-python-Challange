programming_dictionary = {
  "Bug":
  "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "doing action Over and over again"
}

print(programming_dictionary)

# printing value

print(programming_dictionary["Bug"])

#adding values in dictionary

programming_dictionary["variable"] = "Give the name of the data type"

print(programming_dictionary)

#updating the value

programming_dictionary["Loop"] = "this is Updated statment"

print(programming_dictionary)

# wipe dictionary data
programming_dictionary = {}
print(programming_dictionary)

programming_dictionary = {
  "Bug":
  "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "doing action Over and over again"
}

# Looping Dictionary

# methood One

for key in programming_dictionary:
  # printing Key
  print(key)
  # printing value
  print(programming_dictionary[key])
