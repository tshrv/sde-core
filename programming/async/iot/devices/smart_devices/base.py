from abc import ABC, abstractmethod


class SmartDevice(ABC):
    """base class for all smart devices"""
    
    @abstractmethod
    async def connect(self):
        """establish connection"""
        raise NotImplementedError
    
    @abstractmethod
    async def disconnect(self):
        """destroy connection"""
        raise NotImplementedError
