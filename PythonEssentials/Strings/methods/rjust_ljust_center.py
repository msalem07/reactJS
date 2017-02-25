#
# The rjust and ljust string methods return a padded version of the string they are called on, with spaces inserted
# to justify the text. The first argument to both methods is an integer length for the justified string

greeting = 'Hello World'

print(greeting.rjust(15))

print(greeting.ljust(15))

# rjust and ljust say that we want to justify hello world in a string of total length 10. 'Hello World' is 11
# characters so four spaces will be added to its right/left giving us a string of 15 characters with Hello World
# justified right/left

# An optional second argument will specify a fill character other than a space character

print(greeting.ljust(15, '*'))