# # Review:
# # Create a function called greet().
# def greet():

#   # Write 3 print statements inside the function.
#   print("Hello")
#   print("Python")
#   print("Function")

# # Call the greet() function and run your code.

# greet()


def greeting_with_parameter(name):
  print(f"Hello {name}")
  print(f"How are You today {name}?")


fname = input("Please Enter Your name?  ")

greeting_with_parameter(fname)


def greeting_with(name, lname, age):
  print(f"Hello {name} {lname} You are {age} years old")


# This is possitional Argument
greeting_with("Dagmawi", "Lettarik", 25)
# This is keyword argument
greeting_with(lname="Leta", age=26, name="Dagi")
