#! python3

#   The first line of all your Python programs should be a shebang line, which tells your computer that you want Python
#   to execute this program. The shebang line begins with #!, but the rest depends on your operating system.
#       Windows, the shebang line is    #! python3
#       OS X, the shebang line is       #! /usr/bin/env python3
#       On Linux, the shebang line is   #! /usr/bin/python3

#command line arguments are stored in the variable sys.argv
import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)