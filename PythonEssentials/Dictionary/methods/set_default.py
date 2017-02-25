# Sometimes you'll often have to set a value in a dictionary for a certain key only if that key does not already have a
# value. The setdefault method offers a way to do this in one line of code.
# first argument is the key to check for, and the second is the value to set at that key if the key does not exist

dog = {'dog': 'Pooka', 'age': 5}

dog.setdefault('color', 'white')

print(dog)

# If the key does exist, the setdefault method returns the key's value

dog.setdefault('color', 'black')
print(dog)

# Cool character count code

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)