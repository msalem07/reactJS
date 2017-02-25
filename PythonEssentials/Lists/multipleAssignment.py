#
# The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in
# one line of code

# Instead of doing this
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size, color, disposition)

# We can type this line of code
# Note that the number of variables and the length of the list must match exactly or Python will give you a ValueError
cat = ['fat', 'white', 'quiet']
size, color, disposition = cat

print(size, color, disposition)