def compare(dictionary, given_key):
    for key in dictionary:
        if dictionary[given_key]['bid'] > dictionary[key]['bid']:
            dictionary[given_key]['times'] += 1