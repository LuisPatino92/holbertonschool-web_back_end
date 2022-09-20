#!/usr/bin/env python3
"""Function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Docstring placeholder
    """
    delay = await asyncio.sleep(random.uniform(0, max_delay))
    return delay
