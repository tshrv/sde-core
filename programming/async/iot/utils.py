from time import time
from typing import Awaitable, Tuple

from loguru import logger
import asyncio

def timed(task):
    def outer(fn: Awaitable):
        async def inner(*args, **kwargs):
            logger.info(f'{task} started')
            start_time = time()
            resp = await fn(*args, **kwargs)
            logger.info(f'{task} completed in {time() - start_time}s')
            logger.info('--------------------------')
            return resp
        return inner
    return outer

class Runner:
    @classmethod
    async def parallel(cls, *coroutines: Tuple[Awaitable]) -> None:
        await asyncio.gather(*coroutines)

    @classmethod
    async def sequential(cls, *coroutines: Tuple[Awaitable]) -> None:
        for coroutine in coroutines:
            await coroutine