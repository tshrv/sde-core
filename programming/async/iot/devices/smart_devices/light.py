import asyncio

from loguru import logger

from .base import SmartDevice


class Light(SmartDevice):
    """Smart light APIs"""
    
    async def connect(self):
        logger.info('connecting...')
        await asyncio.sleep(1)
        logger.info('connected')

    async def turn_on(self):
        logger.info(f'turning lights on...')
        await asyncio.sleep(3)
        logger.info(f'lights turned on')
    
    async def turn_off(self):
        logger.info(f'turning lights off...')
        await asyncio.sleep(3)
        logger.info(f'lights turned off')
    
    async def disconnect(self):
        logger.info('disconnecting...')
        await asyncio.sleep(1)
        logger.info('disconnected')
