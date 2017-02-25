#!  python3

#   This will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this
#   new text to the clipboard.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)


