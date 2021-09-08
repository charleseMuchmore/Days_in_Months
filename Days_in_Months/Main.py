from functions import *

year = int(input("Enter a year: "))
month = int(input("Enter a month (number): "))
days = days_in_month(year, month)
clear()
month_name = month_name(month)
print(f'There are {days} days in {month_name}, in the year {year}.')



