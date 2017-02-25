#
#   Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use
#   the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes
#   where it left off.

def reverse(data):

    for index in range(len(data)-1, -1, -1):
        yield data[index]

data = ["a", "b", "c", "d", "e", "f", "g"]

for char in reverse(data):
    print(char)

#   The for loop statement calls iter() on the container object. The function returns an iterator object that defines
#   the method __next__() which accesses elements in the container one at a time.
#   Since a function with a yield returns a generator, which is like an iterator, and contains the __next__()
#   implementation the following can also be read in this way
#
#   For what I can understand, it's just a way to create a custom iterator, say you want to add 5 to each data in
#   A list, you could always write

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for digit in range(len(numbers)):
    numbers[digit] += 5

print(numbers)

# or you could define a generator function


def addFive(numbers):
    for digit in range(len(numbers)):
        numbers[digit] += 5
        yield numbers[digit]



# One thing to notice, the generator does not return a list, rather, it returns a single digit. Therefore is memory
# efficient.
# Second, you dont have to get all values at once, generators return a single value when next their next method is
# called on them, this way you can suspend and resume the operation of a function manually

digit = addFive(numbers)

print("The next digit is " + str(next(digit)))
print("The next digit is " + str(next(digit)))

# The function will retain its state and will know what the next number should be

# Third, generators have different entry points.

def echo(value=None):

     print("Execution starts when 'next()' is called for the first time.")
     try:
         while True:
             try:
                 value = (yield value)
             except Exception as e:
                 value = e
     finally:
            print("Don't forget to clean up when 'close()' is called.")
generator = echo(1)
print(next(generator))

print(next(generator))
#You can send a value to the function
print(generator.send(2))

generator.throw(TypeError, "spam")

#Close the generator whenever you dont plan on using it anymore
generator.close()

#Note:  for x in generator
#        yield x
#
#   is equal to
#   yield from generator
