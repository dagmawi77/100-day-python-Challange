modified = 1

def modfied_function():
  global modified
  modified += 1
  print(f"Modifed Number is {modified}")


modfied_function()
print(f"Modifed Number is {modified}")



# other way of modifing global scope

md = 10

def md_function():
  print(f"Modifed Number is {modified}")