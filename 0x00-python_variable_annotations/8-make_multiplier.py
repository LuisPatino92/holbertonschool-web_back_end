#!/usr/bin/env python3
"""tFunction"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Functions
    """
    return lambda x: x * multiplier
