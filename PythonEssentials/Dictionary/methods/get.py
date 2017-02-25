# Dictionaries have a get method that takes two arguments: the key of the value to retrieve and a fallback value to
# return if that key does not exist

picnicItems = {'apples': 5, 'cups': 2}


print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

