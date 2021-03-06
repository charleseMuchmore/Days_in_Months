from os import system, name

def is_leap(year):
    """Checks if a year is a leap year, returns a boolean"""
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def days_in_month(year, month):
    """returns the number of days in a given month, in a given year"""
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    leap = is_leap(year)
    number = month_days[month]
    if month == 2 and leap == True:
        number = 29
        return number
    else:
        number = number
        return number

def month_name(month_num):
    """Takes a number and returns the corresponding month's name as a string"""
    months_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    the_name = months_names[month_num - 1]
    return the_name

def clear():
    """Clears the terminal"""
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')



