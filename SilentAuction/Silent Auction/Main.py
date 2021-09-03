from clear import * 
from compare import *
user_info = {}
cont = True
while cont == True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    user_info[name] = {'bid' : bid, 'times' : 0}
    more = input("Are there an other bidders? Type 'yes' or 'no'. \n")
    number_of_people = 0
    if more == 'yes':
        cont = True
        number_of_people += 1
        clear()
    elif more == 'no':
        cont = False
for key in user_info:
    compare(user_info, key)
for key in user_info:
    number_of_people += 1
for key in user_info:
    num_times = user_info[key]['times']
    if num_times == number_of_people - 1:
        clear()
        print(f'{key} is the winner, bidding ${user_info[key]["bid"]}!')
