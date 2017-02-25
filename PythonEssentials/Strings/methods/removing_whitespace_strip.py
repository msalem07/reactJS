#
# Sometimes you may want to strip off whitespace characters from the left side, right side, or both sides of a string
# The strip string method will return a new string without any whitespace

spacedName = "  Mariano  S       "

print(spacedName+'1')
print(spacedName.strip()+'1')
print(spacedName.lstrip()+'1')
print(spacedName.rstrip()+'1')

#Optionally, a string argument will specify which characters on the ends should be stripped.

spamName = "AAAAAAAAAAAAAAAAAAAMARIANOAAAAAAAAAAAAA";

print(spamName.strip('A'));