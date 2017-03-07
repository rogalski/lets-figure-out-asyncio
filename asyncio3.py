"""
In previous examples there was no concept of corouine result.
Let's change that.
"""
import asyncio

SLEEP_TIMES = [x/10 for x in range(10)]

async def my_first_coroutine(duration):
    await asyncio.sleep(duration)
    return duration


def main():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(my_first_coroutine(x)) for x in SLEEP_TIMES]
    loop.run_until_complete(asyncio.wait(tasks))
    results = [t.result() for t in tasks]
    print(results)
    loop.close()


if __name__ == "__main__":
    main()
