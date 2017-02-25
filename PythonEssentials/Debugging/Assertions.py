#
#   An assertion is a sanity check to make sure your code isn't doing something obviously wrong. These sanity checks are
#   performed by assert statements. If the sanity check fails, then an AssertionError exception is raised. In code, an
#   assert statement consists of the following:
#       The assert keyword
#       A condition
#       A comma
#       A string to display when the condition is False

#   These are for programmer errors, so that you can quickly identify the cause of the bug
#   You can disable assertions by passing the -0 option when running Python


hello = 'Hello World!'

assert hello == 'Hello World!'

hello = '''I'm sorry, Dave. I'm afraid I can't do that.'''

assert hello == "Hello World!"


