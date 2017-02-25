#
#   A task is responsible for executing a coroutine object in an event loop. If the wrapped coroutine yields from a
#   future, the task suspends the execution of the wrapped coroutine and waits for the completion of the future. When
#   the future is done, the execution of the wrapped coroutine restarts with the result or the exception of the future

#   Event loops use cooperative scheduling: an event loop only runs one task at a time. Other tasks may run in parallel
#   if other event loops are running in different threads. While a task waits for the completion of a future, the
#   event loop executes a new task.

#   Don't directly create Task instances: use the ensure_future() function or the AbstractEventLoop.create_task() method

import asyncio

# Example: Parallel execution of tasks

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
loop.close()