#
#   Regular expressions, called regexes for short, are descriptions for a pattern of text. For example, a \d in a regex
#   stands for a digit character--, that is, any single numeral 0 to 9. Regular expressions can be much more
#   sophisticated. I.E. Adding a 3 in curly brackets, {3}, after a pattern is like saying, match this pattern three
#   times
#   so \d\d\d-\d\d\d-\d\d\d\d is equal to \d{3}-\d{3}-\d{4}
#
#   All the regex objects are in the re module, so import it

import re

#   Passing a string value representing your regular expression to re.compile returns a Regex pattern object.

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#or
easyPhoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

#   A regex object's search() method searches the string is is passed for any matches to the regex. The search() method
#   will return None if the regex pattern is not found in the string. If it is found, the search method returns a
#   Match object. Match objects have a group method that will return the actual matched text from the searched string

matchObject = phoneNumberRegex.search('My number is 415-555-4242.')
noMatchObject = phoneNumberRegex.search('I will forget a number in 415-555-424')


print("Phone number found? " + matchObject.group())
try:
    print("Phone number found? " + noMatchObject.group())
except Exception as e:
    print("This is the error: " + str(e))


