#!/usr/bin/env python3
"""Python - Async, The basics of async"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
