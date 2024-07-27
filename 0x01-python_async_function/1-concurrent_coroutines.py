#!/usr/bin/env python3
"""multiple coroutines"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
"""
Import wait_random from the previous
python file that you’ve written and write
Parameters: n,  max_delay, wait_random
Returns: the list of all the delays (float values)
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
