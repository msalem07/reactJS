#
# You can determine whether a value is or isn't in a list with the in and not in operators

greetings = ['hello', 'hi', 'howdy', 'heyas']


def isInArray(word):

    global greetings
    return word in greetings


def isNotInArray(word):
    global greetings
    return word not in greetings


result = isInArray('cat')
result2 = isNotInArray('cat')
print(result, result2, sep=', ')

