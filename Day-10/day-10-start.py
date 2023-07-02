def format_name(f_name, l_name):
  """ Adding Doc String For Function the above faction is used for
  formaing the name like this => Dagmawi Letarik
  """
  # multiple return statment
  if f_name == "" and l_name == "":
    """
    Or it Used For multi line commenting 
    also
    """
    return "You Insert Nothing"
  f_name = f_name.title()
  l_name = l_name.title()
  full_name = f_name + " " + l_name
  return full_name


formated_string = format_name(input("What is Your first name? "),
                              input("What is Your Last Name ? "))
print(formated_string)
format_name()
