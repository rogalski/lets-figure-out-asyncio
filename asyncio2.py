"""
asyncio with custom callbacks for results.

Callback here simply advances progressbar.
"""

import asyncio
import time

SLEEP_TIMES = [1 for x in range(100)]


async def my_first_coroutine(duration):
    await asyncio.sleep(duration)


async def progress_bar(total_count):
    completed_count = 0
    while completed_count < total_count:
        await asyncio.sleep(0.01)
        completed_count = COMPLETED_COROUTINES
        print("\rCompleted: [", "#" * completed_count, " " * (total_count - completed_count), "]", end="", flush=True)
    print("\rCompleted: [", "#" * completed_count, " " * (total_count - completed_count), "]")


COMPLETED_COROUTINES = 0


def completed(future):
    global COMPLETED_COROUTINES
    COMPLETED_COROUTINES += 1


def main():
    loop = asyncio.get_event_loop()
    futures = [asyncio.ensure_future(my_first_coroutine(x), loop=loop) for x in SLEEP_TIMES]
    for future in futures:
        future.add_done_callback(completed)
    reporter = asyncio.ensure_future(progress_bar(len(futures)), loop=loop)
    loop.run_until_complete(reporter)
    loop.close()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Async code stopped after", time.time() - start_time, "seconds")
