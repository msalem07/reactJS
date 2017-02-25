#
# List values have an index() method that can be passed a value,
# and if that value exists in the list, the index of the value is returned; if not Python produces
# a ValueError

greetings = ['hello', 'hi', 'howdy', 'heyas', 'howdy']

print(greetings.index('hello'))
print(greetings.index('heyas'))

try:
    print(greetings.index('What up'))
except ValueError:
    print('This value is not an acceptable greeting')

# If there are duplicates, the index of its first appearance is returned
print(greetings.index('howdy'))