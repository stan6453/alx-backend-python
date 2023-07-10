#!/usr/bin/env python3
"""return a task"""

import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    """return a task"""
    return asyncio.create_task(wait_random(max_delay))
