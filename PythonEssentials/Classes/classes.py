

class MyClass:

    # basically the constructor, it can have arguments

    def __init__(self, argumentOne, argumentTwo):
        self.data = argumentOne
        self.data2 = argumentTwo

    def f(self):
        return 'hello world!'

x = MyClass(1, 2)

# You can call the objects data attributes like this
print(x.data, x.data2)

# Data attributes don't need to be declared, they spring into existence when they are first assigned to
x.counter = 1

print(x.counter)

# You can delete it too
del x.counter

# You can also call the class methods
print(x.f())

# or you can save it in another variable and call it whenever you need it
xfunction = x.f

print(xfunction())

