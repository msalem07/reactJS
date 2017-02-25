#
#   The pyperclip module has copy and paste functions that can sent text to and receive text from your computer's
#   clipboard.

import pyperclip

#pyperclip.copy('Hello world!!!!!!!!!!!!!!!')

#print(text)
#Now paste underneath


# Uncomment the bottom but comment top so this works
#copy this sentence
# For example, if I copied this sentence to the clipboard and then called paste(), it would look like this: '

text = pyperclip.paste()
print(text)