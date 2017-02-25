#
# The join method is useful when you have a list of strings that need to be joined together into a single string value

space = ' '
comma = ','

r_space = space.join(['cats', 'rats', 'bats'])
r_comma = comma.join(['cats', 'rats', 'bats'])

print(r_space)
print(r_comma)

# split method does the opposite. It's called on a string value and returns a list of strings.

sample_string = 'My name is Mariano'

print(sample_string.split())

# By default, the string is split wherever whitespace characters such as the space, tab, or newline characters are found
# You can pass a delimiter string to the split method to specify a different string to split upon.

print(sample_string.split('m'))

