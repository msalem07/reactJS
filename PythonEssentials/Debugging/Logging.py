#
#   Logging is a great way to understand what's happening in your program and in what order its happening.
#   To enable the logging module to display log messages on your screen as your program runs import logging
#   To disable add a single logging.disable(logging.CRITICAL) call

#   Logging levels provide a way to categorize your log messages by importance
#   level               logging Function
#   DEBUG               logging.debug()         Used for small details
#   INFO                logging.info()          Used to record information on general events in your program
#   WARNING             logging.warning()       used to indicate a potential problem that doesnt prevent the program
#                                               from working but it might do so in the future
#   ERROR               logging.error()         Used to record an error that caused the program to fail
#   CRITICAL            logging.critical()      Used to indicate a fatal error
#
#   Logging to a file
#   the basicConfig takes a filename keyword argument, filename='myProgramLog.txt'
import logging

#   Basic Configuration

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug( 'i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

#   Passing logging.DEBUG to the basic configuration lets you see all the messages from all the logging levels
#   Change this if you're interested only in i.e. Errors    level=logging.ERROR, this will display only error and
#   critical

#   Disable logging
#   The logging.disable function disables loggings. Simply pass the function a logging level, and it will suppress all
#   log messages at that level or lower.

#   logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')


