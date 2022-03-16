import asyncio

from loguru import logger

from .base import SmartDevice


class Speaker(SmartDevice):
    """Smart speaker APIs"""
    
    async def connect(self):
        logger.info('connecting...')
        await asyncio.sleep(1)
        logger.info('connected')

    async def start_radio(self):
        logger.info(f'tuning radio...')
        await asyncio.sleep(3)
        logger.info(f'radio tuned in')
    
    async def stop_radio(self):
        logger.info(f'stopping radio...')
        await asyncio.sleep(3)
        logger.info(f'radio stopped')

    async def disconnect(self):
        logger.info('disconnecting...')
        await asyncio.sleep(1)
        logger.info('disconnected')
