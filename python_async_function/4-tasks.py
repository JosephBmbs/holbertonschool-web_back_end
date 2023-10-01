#!/usr/bin/env python3

"""Function that executes multiple coroutines at the same time"""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that calls wait_random n times"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
