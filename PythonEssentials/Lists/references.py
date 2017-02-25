import copy

#
# When you assign a list to a variable, you are actually assigning a list reference to the variable.

animals = ['cat', 'dog', 'bat', 'elephant']

copyOfAnimals = animals

copyOfAnimals[2] = 'penguin'

print(copyOfAnimals)
print(animals)

# Python uses references whenever variables must store values of mutable data types

# Whenever you need to duplicate a list, Python provides a module named copy that provides both the copy() and
# deepcopy() functions.

animals = ['cat', 'dog', 'bat', 'elephant']

copyOfAnimals = copy.copy(animals)

copyOfAnimals[2] = 'penguin'

print(copyOfAnimals)
print(animals)

# deepcopy is used whenever a list contains a list