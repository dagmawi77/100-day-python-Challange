def format_name(f_name, l_name):
  f_name = f_name.title()
  l_name = l_name.title()
  full_name = f_name + " " + l_name
  return full_name


formated_string = format_name("DAGMAWI", "LETARIK")
print(formated_string)