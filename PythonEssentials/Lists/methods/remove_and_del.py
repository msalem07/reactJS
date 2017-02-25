#
# The remove method is passed the value to be removed from the list it is called on

animals = ['cat', 'bat', 'rat', 'elephant', 'rat']

animals.remove('bat')

print(animals)

# Attempting to delete a value that does not exist in the list will result in a ValueError error

try:
    animals.remove('dog')
except ValueError:
    print('This animal is not in the animals array', animals)

# If the value appears multiple times in the list, only the first instance of the value will be removed

print(animals)
animals.remove('rat')
print(animals)

# The del statement is used to delete items in a list when you know the index
del animals[2]
print(animals)