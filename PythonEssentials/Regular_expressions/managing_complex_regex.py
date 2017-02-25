#
#   To spread the regular expression over multiple lines with comments pass the variable re.VERBOSE as the second
#   argument to re.compile()

import re

phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?              #area code without or with parenthesis
                            (\s|-|\.)?                      #separator can be a space,tab,newline, or a -, or a .
                            \d{3}                           #first three digits
                            (\s|-|\.)?                      #another separator
                            \d{4}                           #next four digits
                            (\s*(ext|x|ext.)\s*\d{2,5})?    #extension
                            )''', re.VERBOSE)
