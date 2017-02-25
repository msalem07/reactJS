#
#   Instance variables are for data unique to each instance, and class variables are for attributes and methods
#   shared by all instances of the class

class Dog:

    kind = 'canine'                 # class variable shared by all instances

    def __init__(self, name):
        self.name = name            #instance variable unique to each instance


fido = Dog('Fido')
buddy = Dog('Buddy')

print(buddy.kind, buddy.name)
print(fido.kind, fido.name)

# Note: Data attributes override method attributes with the same name