def compare(dictionary, given_key):
    for key in dictionary:
        bidindict = dictionary[key]['bid']
        # timesindict = dictionary[key]['times']
        bidingiven_val = dictionary[given_key]['bid']
        # timesingiven_val = dictionary[given_key]['times']
        if bidingiven_val > bidindict:
            # print(f'{bidingiven_val} is greater than {bidindict}')
            dictionary[given_key]['times'] += 1