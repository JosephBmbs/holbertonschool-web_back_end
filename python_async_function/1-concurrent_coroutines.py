#!/usr/bin/env python3
"""Python - Async task 1"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Return the list of all the delays in ascending order"""
    delays = []
    for i in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delays)]
