#!/usr/bin/env python3

"""Function that creates an asyncio task"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
