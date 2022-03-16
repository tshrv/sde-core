import asyncio

from loguru import logger

from .base import SmartDevice


class Toilet(SmartDevice):
    """Smart toilet APIs"""
    
    async def connect(self):
        logger.info('connecting...')
        await asyncio.sleep(1)
        logger.info('connected')

    async def flush_toilet(self):
        logger.info(f'flushing toilet...')
        await asyncio.sleep(3)
        logger.info(f'toilet flushed')
    
    async def clean_toilet(self):
        logger.info(f'cleaning toilet...')
        await asyncio.sleep(3)
        logger.info(f'toilet cleaned')

    async def disconnect(self):
        logger.info('disconnecting...')
        await asyncio.sleep(1)
        logger.info('disconnected')
