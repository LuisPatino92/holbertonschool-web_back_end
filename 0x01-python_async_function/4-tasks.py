#!/usr/bin/env python3
"""Function"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int,  max_delay: int) -> List[float]:
    """
    Docstring Placeholder
    """
    tasks_done = list()
    tasks_process = list()
    for _ in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(
            lambda future_obj: tasks_done.append(future_obj.result()))
        tasks_process.append(task)
    await asyncio.gather(*tasks_process)
    return tasks_done
