#
#   There are times when you want to match a set of characters but the shorthand characters classes are too broad. You
#   can define your own character class using square brackets.
import re
#   Matches any vowel, lower or uppercase

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

print(mo)

#   You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9]
#   will match all lowercase letters, uppercase letters, and numbers.

#   By placing a caret character (^) just after the character class's opening bracket, you can make a negative
#   character class. A negative character class will match all the characters that are not in the character class

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

#   You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning
#   of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must
#   end with this regex pattern.

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world')
print(mo.group())

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
mo2 = endsWithNumber.search('Your number is forty two')
print(mo.group())
print(mo2)

#   The r'^\d+$' expression string matches strings that both begin and end with one or more numeric characters

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234556790')
mo2 = wholeStringIsNum.search('123456ert654')
print(mo)
print(mo2)

#   The . character in a regular expression is called a wildcard and will match any character except for a newline.
#   Remember that the dot character will match just one character.

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo)

#   Sometimes you will want to match. For example, say you want to match the string 'First Name:', followed by any and
#   all text, folowed by 'Last Name:' and then followed by anything again. You can use the dot-star (.*) to stand
#   in for that "anything". Remember . means any single character except a newline, and * means 0 or more preceding
#   characters.

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1),mo.group(2))

#   The dot-star (.*) uses greedy mode: It will always try to match as much text as possible. To match any and all text
#   in a nongreedy fashion, use the dot, start and question mark (.*?)

nongreedyRegex = re.compile(r'<.*?>')
greedyRegex = re.compile(r'<.*>')

mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')

print(mo.group(), mo2.group())

#   The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(),
#   you can make the dot character match all characters, including the newline character

noNewlineRegex = re.compile('.*')
newlineRegex = re.compile('.*',re.DOTALL)
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

print(mo,mo2)
