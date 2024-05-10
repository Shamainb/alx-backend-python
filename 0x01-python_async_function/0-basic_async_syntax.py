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
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
