#
#   You can add iterator behaviour to your classes. Define an __iter__() method which returns an object with a
#   __next__() method. If the class defines __next__() then __iter__() can just return self.

class Reverse:

    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('spam')

for char in rev:
    print(char)
