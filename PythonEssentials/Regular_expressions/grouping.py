#   async io. python, check it out
#   You can add parentheses to create groups in the regex:

import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

matchObject = phoneNumberRegex.search('My number is 415-555-4242.')

print(matchObject.group(1))
print(matchObject.group(2))
print(matchObject.group(0))

#   if you would like to retrieve all the groups at once, use the groups() method

areaCode, mainNumber = matchObject.groups()
print(areaCode,mainNumber)

# You can use the |, called a pipe, to match one of many expressions. If both are present the first occurrence of
# matching text will be returned as the match object. Note: You can find all matching occurrences with the findall()
# method

heroRegex = re.compile(r'Batman|Tina Fey')
matchObject = heroRegex.search('Batman and Tina Fey.')
matchObject2 = heroRegex.findall('Batman and Tina Fey.')
print(matchObject.group())
print(matchObject2)

# You can also use the pipe to match one of several patterns as part of your regex. i.e
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#   The ? character flags the group that precedes it as an optional part of the pattern. You can think of the ? as
#   saying Match zero or one of the group preceding this question mark.

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

#   The * means "match zero or more" -the group that precedes the star can occur any number of times in the text

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batwowowowowowowowowowoman')
print(mo3.group())

#   The + means match one or more. The group preceding a plus must appear at least once
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batman')
print(mo2)


