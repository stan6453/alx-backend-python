#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start_time)/n
