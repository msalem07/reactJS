#
#   What I understand so far:
#   In order to run an asynchronous event, you need a function that can be entered, paused, and exited at any point in
#   time. This is why you need to either define a function with async def, or create a generator function
#   If the latter, these generator functions should be decorated with @asyncio.coroutine. These methods, if you haven't
#   caught on, are called coroutines

#   Coroutines then can suspend the function:
#       result = await future or    result = yield from future
#       result = await coroutine or result = yield from coroutine
#       return expression
#       raise exception

#   Calling a coroutine does not start its code running. the coroutine object returned by the call doesn't do anything
#   until you schedule its execution.
#   Two basic ways to start it running:
#       call await coroutine or yield from coroutine from another coroutine
#       schedule its execution using the ensure_future() function or the AbstractEventLoop.create_task()
#
#   Note Coroutine (and tasks) can only run when the event loop is running

import asyncio
import time

# Example one

async def hello_world():
    print("Hello World")
    time.sleep(5)

loop = asyncio.get_event_loop()

loop.run_until_complete(hello_world())
print("My hello world function is done!")


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop2 = asyncio.get_event_loop()
loop2.run_until_complete(print_sum(1, 2))
loop2.close()