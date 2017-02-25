#
# The functions list() and tuple() will return list and tuple versions of the values passed to them

numbers = (1, 2, 3, 4, 5, 6)

animals = ['cat', 'bat', 'dog', 'elephant']

t_Animals = tuple(animals)
l_numbers = list(numbers)

print(type(animals), type(t_Animals), type(numbers), type(l_numbers))

# Works on strings too

s_Animal = list(animals[3])
print(s_Animal, type(s_Animal))