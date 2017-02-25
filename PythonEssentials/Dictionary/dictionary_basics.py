#
# Dictionary is a collection of many values. Indexes for dictionaries can use many different data types, not just
# integers. Basically Objects

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])

# Trying to access a key that does not exist will result in a KeyError error message

try:
    myCat['superpowers']
except KeyError:
    print('Sorry, your cat is just an ordinary cat')

