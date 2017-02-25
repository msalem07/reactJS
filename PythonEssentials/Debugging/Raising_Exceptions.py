#
#   You can raise your own exceptions in your code. Exceptions are raised with a raise statement.
#   In code, a raise statement consists of the following
#       The raise keyword
#       A call to the Exception() function
#       A string with a helpful error message passed to the Exception() function

number = 10

try:
    if number > 5:
        raise Exception('Number is greater than 5')
except Exception as err:
    print('An exception happened: ' + str(err))