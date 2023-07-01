def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # for index,new_month in enumerate(month_days):
  #   final_new_month = int(month - 1)
  #   if index == final_new_month:
  #     return month_days[index]
  if is_leap(year) and month == 2:
    return 29
  print(month_days[month - 1])


#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
