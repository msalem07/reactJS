#
# You can use negative intergers for the indexes. The value -1 refers to the last index in a list, -2 refers to the
# second to last, and so on.

animals = ['cat', 'bat', 'rat', 'elephant']

print(animals[3], animals[-1])

# You can also slice values from a list, a slice is typed between square brackets, like an index, but it has two
# integers separated by a colon

print(animals[0:4])
print(animals[1:3])
print(animals[0:-1])

# As a shortcut, you can leave out one or both of the idnexes on either side of the colon in the slice.
# Leaving out the first index is the same as using 0; leaving out the second index is the same as using the length of
# the list

print(animals[:2])
print(animals[1:])
