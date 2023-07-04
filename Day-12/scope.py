################### Scope ####################

enemies = 1


def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope


def local_scope():
  local_scope_variable = "I am local"
  print(local_scope_variable)


local_scope()

# if you call variable out side of scop like this print(local_scope_variable)
# print(local_scope_variable)

# There is No Block scope
level = 3
enemies = ["Skelton", "Zumba", "Alian"]

if level < 5:
  new_enemie = enemies[0]

print(new_enemie)
