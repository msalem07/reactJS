#
# if you import the pprint module into your programs, you'll have acess to the pprint() and pformat functions that will
# pretty print a dictionary's values

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)

# If you want to obtain the prettified text as a string value instead of displaying it on the screen, call
# pprint.pformat() instead

formattedText = pprint.pformat(count)

print(formattedText)