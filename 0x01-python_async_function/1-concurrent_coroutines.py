#!/usr/bin/env python3
"""Module"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int,  max_delay: int) -> List[float]:
    """
    Docstring placeholder
    """
    tasks_done =  []
    tasks_process = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(
            lambda future_obj: tasks_done.append(future_obj.result()))
        tasks_process.append(task)
    
    await asyncio.gather(*tasks_process)
    return tasks_done
