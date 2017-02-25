#
#   Futures are like Promises in javascript. A Future is an object that is supposed to have a result in the future.

import asyncio

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = loop.create_future()

# The future is used to link slow_operation() to got_result(). When slow operation() is done, got_result() is called
# with the result

asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()
