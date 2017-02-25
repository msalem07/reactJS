#
# The upper and lower string methods return a new string where all the letters in the original string have been
# converted to uppercase or lowercase, respectively.

greeting = 'Hello world!'

u_greeting = greeting.upper()

l_greeting = greeting.lower()

print(u_greeting, l_greeting)

# These methods do not change the string itself but return new string values

print(greeting)

# The isupper and islower methods will return a boolean true value if the string has at least one letter and all the
# letters are uppercase or lowercase, respectively. Otherwise it returns false

print(greeting.isupper())
print(greeting.islower())
print(u_greeting.isupper())

# There are other several methods that have name beginning with the word is. These methods return a Boolean value that
# describes the nature of the string. Here aer some common isX string methods

# isalpha returns true if the string consist of only letters and is not blank

print('Is alpha 1: ', greeting.isalpha())
print('Is alpha 2: ', 'Hello'.isalpha())

# isalnum returns true if the string consists of only numbers and letters and is not blank

print('Is alnum 1: ', greeting.isalnum())
print('Is alnum 2: ', '1234abc'.isalnum())

# isdecimal returns true if the string consists only of numeric characters and is not blank

print('Is decimal 1', greeting.isdecimal())
print('Is decimal 2', '123456'.isdecimal())

# ispace returns true if the string consists only of spaces, tabs, and newlines and is not blank
print('Is space 1', greeting.isspace())
print('Is space 2', '      '.isspace())

# istitle returns true if the string consists only of words that begin with an uppercase followed by only lowercase
# letters

print('Is title 1', greeting.istitle())
print('Is title 2', 'Hello World!'.istitle())



