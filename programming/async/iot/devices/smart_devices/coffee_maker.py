import asyncio

from loguru import logger

from .base import SmartDevice


class CoffeeMaker(SmartDevice):
    """Smart coffee maker APIs"""
    
    async def connect(self):
        logger.info('connecting...')
        await asyncio.sleep(1)
        logger.info('connected')

    async def make_coffee(self):
        logger.info(f'pouring coffee...')
        await asyncio.sleep(3)
        logger.info(f'coffee served')

    async def disconnect(self):
        logger.info('disconnecting...')
        await asyncio.sleep(1)
        logger.info('disconnected')
