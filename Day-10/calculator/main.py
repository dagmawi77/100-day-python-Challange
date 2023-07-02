from art import logo


def Add(numOne, numTwo):
  """Addtion Function It take 
  two numbers from the user"""
  return numOne + numTwo


def Multiplication(numOne, numTwo):
  """Multiplication Function It take 
  two numbers from the user"""
  return numOne * numTwo


def Devision(numOne, numTwo):
  """Devision Function It take 
  two numbers from the user"""
  return numOne / numTwo


def Substarction(numOne, numTwo):
  """Substarction Function It take 
  two numbers from the user"""
  return numOne / numTwo


# Creating Dectinary for operater sign
operation = {"+": Add, "*": Multiplication, "/": Devision, "-": Substarction}


def calculation():
  print(logo)
  num_1 = float(input("What is the first number? "))

  for symbol in operation:
    print(symbol)
  other_operation = True
  while other_operation:
    pick_opration = input("Pick an operan  ")
    num_2 = float(input("What is the next number? "))
    calculation_functon = operation[pick_opration]
    answer = calculation_functon(num_1, num_2)

    print(f"{num_1} {pick_opration} {num_2} = {answer}")

    user_option = input(
      f"Type 'y'  to Continue Calculating with {answer} type 'n' to exit ")
    if user_option == 'y':
      num_1 = answer
    elif user_option == 'n':
      other_operation = False
      print(f"The Final Answer is {num_1} {pick_opration} {num_2} = {answer}")
      calculation()


calculation()
