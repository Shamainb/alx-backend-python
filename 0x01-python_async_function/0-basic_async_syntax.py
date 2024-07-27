#!/usr/bin/env python3
import random
import asyncio

"""
Asynchronous coroutine that waits for a
random delay between 0 and max_delay (inclusive) seconds.
Parameters:
max_delay (int): The upper limit of the random delay (default: 10)

Returns:
float: The random delay value
"""


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.'''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
