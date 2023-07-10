#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """

import asyncio
from typing import List, Union, Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[Union[int, float]]:
    results: List[Union[int, float]] = []
    coroutines: List[Coroutine] = [add_to_list(n, max_delay, results)
                                   for n in range(n)]

    await asyncio.gather(*coroutines)

    return results


async def add_to_list(n: int, max_delay: int,
                      results: List[Union[int, float]]):
    delay = await wait_random(max_delay)
    results.append(delay)
