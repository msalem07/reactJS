#
# There are three dictionary methods that will return list-like values of the dictionary's keys, values, or both
# The values returned by these methods are not true lists: They cannot be modified and do not have an append() method
# but can be used in for loops

alien = {'color': 'red', 'age': 42}

for v in alien.values():
    print(v)

for v in alien.keys():
    print(v)

for v in alien.items():
    print(v)

# If you do want a list, pass its list-like return value to the list function

l_alien = []

for v in alien.items():

    l_alien += list(v)

print(l_alien)

#or

l_alien_2 = list(alien.keys())
print(l_alien_2)

# if you want a list of all the elements, use the one that iterates over the items, doing list(alien.items() returns
# a list with tuples in it\


l_alien_2 = list(alien.items())
print(l_alien_2)


# You can also use the multiple assignment trick in a for loop to assign the key and value to separate variables

for c, a in alien.items():
    print('Key: ' + c + ' Value: ' + str(a))



