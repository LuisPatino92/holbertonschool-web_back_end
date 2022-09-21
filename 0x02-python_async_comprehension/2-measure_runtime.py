#!/usr/bin/env python3
"""Module"""

import time
import asyncio


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Docstring placeholder
    """
    start = time.perf_counter()

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]

    await asyncio.gather(*tasks)

    stop = time.perf_counter()
    
    return stop - start
