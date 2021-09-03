from clear import * 

def compare(dictionary, given_key):
    for key in dictionary:
        bidindict = dictionary[key]['bid']
        # timesindict = dictionary[key]['times']
        bidingiven_val = dictionary[given_key]['bid']
        # timesingiven_val = dictionary[given_key]['times']
        if bidingiven_val > bidindict:
            # print(f'{bidingiven_val} is greater than {bidindict}')
            dictionary[given_key]['times'] += 1

user_info = {}

cont = True
while cont == True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    a = user_info[name] = {'bid' : bid, 'times' : 0}
    yesno = input("Are there an other bidders? Type 'yes' or 'no'. \n")
    if yesno == 'yes':
        cont = True
        clear()
    elif yesno == 'no':
        cont = False

for key in user_info:
    compare(user_info, key)

number_of_pairs = 0
for key in user_info:
    number_of_pairs += 1


for key in user_info:
    num_times = user_info[key]['times']
    numtimes = num_times - 1
    if num_times == number_of_pairs - 1:
        print(f'{key} is the winner, bidding {user_info[key]["bid"]}!')
        
      


#TODO:
# make it so that when a user types an invalid input for bid, it gives them a more user friendly error message