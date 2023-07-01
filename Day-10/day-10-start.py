def format_name(f_name, l_name):
  # multiple return statment
  if f_name == "" and l_name == "":
    return "You Insert Nothing"
  f_name = f_name.title()
  l_name = l_name.title()
  full_name = f_name + " " + l_name
  return full_name


formated_string = format_name(input("What is Your first name? "),
                              input("What is Your Last Name ? "))
print(formated_string)