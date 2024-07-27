#!/usr/bin/env python3
"""Create a measure_time function"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return total_time / n.

    Args:
    n (int): The number of times to call wait_random.
    max_delay (int): The maximum delay for wait_random.

    Returns:
    float: The average execution time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
