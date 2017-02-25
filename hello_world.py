import random


print("Hello world")

eggs = 29


def hello():
    global eggs
    eggs = 20
    print('Howdy!')
    return None


balance = input()


def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


for i in range(5):
    hello()

spam(0)
print(eggs)

spam = [1, 2, 3, 4, 5]


try:
    print(spam[:4])
    spam[5]
except IndexError:
    print("The index you're trying to reach is not available")


def addNumberToList(number):
    global spam
    spam += [number]
    for m in range(len(spam)):
        print('Index ' + str(m) + ' in the array is: ' + str(spam[m]))
    return None


addNumberToList(6)
print(spam)

