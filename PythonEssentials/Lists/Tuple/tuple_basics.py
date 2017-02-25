#
# Almost identical to the list data type, except in two ways:
# First, tuples are typed with parentheses

animals = ('cat', 'dog', 'rat', 'elephant')

# Tuples cannot have their values modified

try:
    animals[0] = 'penguin'
except TypeError:
    print('You cannot change my value')

# If you only have one value in the tuple, leave a trailing comma so Python know it is actually a tuple and not a string

greetings1 = ('hello',)
greetings2 = ('howdy')
print(type(greetings1), type(greetings2))