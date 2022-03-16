import asyncio

from loguru import logger

from .base import SmartDevice


class Geyser(SmartDevice):
    """Smart geyser APIs"""
    
    async def connect(self):
        logger.info('connecting...')
        await asyncio.sleep(1)
        logger.info('connected')

    async def start_heating(self):
        logger.info(f'starting heating...')
        await asyncio.sleep(3)
        logger.info(f'heating started')
    
    async def stop_heating(self):
        logger.info(f'stopping heating...')
        await asyncio.sleep(3)
        logger.info(f'heating stopped')

    async def disconnect(self):
        logger.info('disconnecting...')
        await asyncio.sleep(1)
        logger.info('disconnected')
