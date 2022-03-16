from typing import List

from .device_types import DeviceType
from .smart_devices import CoffeeMaker, Geyser, Light, Speaker, Toilet


class DeviceFactory:
    MAPPING = {
        DeviceType.COFFEE_MAKER: CoffeeMaker,
        DeviceType.GEYSER: Geyser,
        DeviceType.LIGHT: Light,
        DeviceType.SPEAKER: Speaker,
        DeviceType.TOILET: Toilet,
    }

    @classmethod
    def build(cls, device_type: DeviceType):
        device_class = cls.__get_mapping().get(device_type)
        return device_class()
    
    @classmethod
    def build_many(cls, device_types: List[DeviceType]):
        return [cls.build(device_type=device_type) for device_type in device_types]

    @classmethod
    def __get_mapping(cls):
        return cls.MAPPING
