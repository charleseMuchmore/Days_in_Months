from os import system, name

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:         
                leap = True
            else:
                leap = False
        else:
            leap = True  
    else:
        leap = False  
    return leap

def days_in_month(year, month):
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
    months_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    the_name = months_names[month_num - 1]
    return the_name

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')



