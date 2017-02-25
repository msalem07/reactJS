#
# You can place an r before the beginning quotation mark of a string to make it a raw string. A raw string completely
# ignores all escape characters and prints any backslash that appears in the string.

print(r'That is Carol\'s cat.')

# While you can use the \n escape character to put a newline into a string, it is often easier to use multiline strings.
# Multiline string in Python begins and ends with either three single quotes or three double quotes.

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

#
''' A multiline string is often used for comments that span multiple lines.
    I still like the hashtag but this works too!
'''
#

# Strings use indexes and slices the same way lists do

greeting = "Hello world!"
print(greeting[0])
print(greeting[-1])
print(greeting[:5])