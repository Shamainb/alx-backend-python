#!/usr/bin/env python3
"""a type-annotated function"""

import math


def floor(n: float) -> int:
    """
    Return the floor of the given float.

    Args:
        n (float): The input float number.

    Returns:
        int: The floor value of n.
    """
    return math.floor(n)
