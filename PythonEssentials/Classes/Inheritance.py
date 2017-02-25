#
#   Derived classes may override methods of their base classes. All methods in Python are effectively virtual


class Animals:

    type = 'animal'

    def sound(self):

        return '????'


class Dogs(Animals):

    type = 'canine'

    def sound(self):

        return 'wooof'

class Cats(Animals):
    pass


dog = Dogs()
cat = Cats()

print(dog.type, dog.sound())
print(cat.type, cat.sound())

