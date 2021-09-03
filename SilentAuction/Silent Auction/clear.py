from os import system, name
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

# print("hello")
# a = input("clear (c) or not clear (nc) ")
# if a == "c":
#     clear()

