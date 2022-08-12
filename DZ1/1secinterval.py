import threading
import asyncio
import time
from asyncio import sleep

# threading
"""
def times(x):
    for i in reversed(range((x)+1)):
        print(i)
        time.sleep(1)

def help_times(x):
    t1 = threading.Thread(target=times,args=(x,))
    t2 = threading.Thread(target=times,args=(x,))
    t3 = threading.Thread(target=times,args=(x,))
    t4 = threading.Thread(target=times,args=(x,))
    t5 = threading.Thread(target=times,args=(x,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

help_times(2)
"""

# asyncio

async def times(x):
    for i in reversed(range((x)+1)):
        print(i)
        await sleep(1)

async def main(x):
    t1 = asyncio.create_task(times(x))
    t2 = asyncio.create_task(times(x))
    t3 = asyncio.create_task(times(x))
    t4 = asyncio.create_task(times(x))
    t5 = asyncio.create_task(times(x))

    await t1
    await t2
    await t3
    await t4
    await t5

loop = asyncio.get_event_loop()
loop.run_until_complete(main(2))

# Без разницы, просто asyncio современнее и больше возможностей