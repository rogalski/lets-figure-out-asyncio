"""
Very basic sample of asyncio capabilities

my_first_coroutine mimics a very typical case where asyncio shines.
Coroutines are long-living callables with small CPU usage - e.g.
HTTP request sent to server where we wait for response. Here this
waiting is mimicked by asyncio.sleep()

Alternative with blocking code is also shown.

Total execution time may be estimated as:
- total waiting time for blocking case
- longest waiting time for non-blocking case
"""

import time
import asyncio

SLEEP_TIMES = range(1, 4)

async def my_first_coroutine(duration):
    await asyncio.sleep(duration)


def my_first_blocking_routine(duration):
    return time.sleep(duration)


def main():
    [my_first_blocking_routine(x) for x in SLEEP_TIMES]


def main_asyncio():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(my_first_coroutine(x)) for x in SLEEP_TIMES]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Blocking code stopped after", time.time() - start_time, "seconds")
    start_time = time.time()
    main_asyncio()
    print("Async code stopped after", time.time() - start_time, "seconds")
