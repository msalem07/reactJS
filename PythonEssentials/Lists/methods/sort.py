#
# Lists of number values or lists of strings can be sorted with the sort() method.

numbers = [2, 5, 3.14, 1, -7]

numbers.sort()

print(numbers)

animals = ['ants', 'cats', 'dogs', 'badgers', 'elephants']

animals.sort()

print(animals)

# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order

animals.sort(reverse=True)
print(animals)

# Only works with list of the same type ('string', ints, objects?(don't know this yet); TypeError is thrown
# sort uses ASCIIbetical order, so uppercases come before lowercases
# if you need to sort the values in regular alphabetical order, pass str.lower for the key keyword

letters = ['A', 'b', 'C', 'd', 'E']
letters.sort()
print(letters)

letters.sort(key=str.lower)
print(letters)
