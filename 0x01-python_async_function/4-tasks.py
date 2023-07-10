#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called."""

import asyncio
from typing import List, Union, Coroutine

task_wait_random = __import__('3-tasks').task_wait_random



async def task_wait_n(n: int, max_delay: int) -> List[Union[int, float]]:
    results: List[Union[int, float]] = []
    coroutines: List[Coroutine] = [add_to_list(n, max_delay, results)
                                   for n in range(n)]

    await asyncio.gather(*coroutines)

    return results


async def add_to_list(n: int, max_delay: int,
                      results: List[Union[int, float]]):
    delay = await task_wait_random(max_delay)
    results.append(delay)