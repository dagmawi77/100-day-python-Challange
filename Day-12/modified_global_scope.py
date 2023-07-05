################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2

  
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# There is No Block scope
# level =3
# enemies = ["Skelton","Zumba","Alian"]

# if level < 5:
#   new_enemie = enemies[0]

# print(new_enemie)

# Modifing Global scope

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
  print(f"Modifed Number is {md}")
  return md+10

md_function()
print(f"Modifed Number is {md}")
md_final = md_function();
print(md_final)
