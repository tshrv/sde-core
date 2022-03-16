import asyncio
import time

from loguru import logger

from devices import DeviceFactory, DeviceType
from utils import timed, Runner


class Routine:
    """
    Daily routine taks in a smart home
    """
    def __init__(self, device_factory=DeviceFactory, runner=Runner) -> None:
        self.coffee_maker, self.geyser, self.light, \
        self.speaker, self.toilet = device_factory.build_many(device_types=[
            DeviceType.COFFEE_MAKER,
            DeviceType.GEYSER,
            DeviceType.LIGHT,
            DeviceType.SPEAKER,
            DeviceType.TOILET,
        ])
        self.runner = runner()
    
    @timed(task='morning routine')
    async def morning_routine(self):
        """
        Morning Routine
        - start radio
          - connect speaker
          - start radio
        - turn on geyser
          - connect geyser
          - turn on heating
        - turn on light
          - connect light
          - turn on light
        - make coffee
          - connect coffee maker
          - make coffee
        """
        await self.runner.parallel(
          self.runner.sequential(
            self.speaker.connect(),
            self.speaker.start_radio(),
          ),
          self.runner.sequential(
            self.geyser.connect(),
            self.geyser.start_heating(),
          ),
          self.runner.sequential(
            self.light.connect(),
            self.light.turn_on(),
          ),
          self.runner.sequential(
            self.coffee_maker.connect(),
            self.coffee_maker.make_coffee()
          )
        )

    @timed(task='night routine')
    async def night_routine(self):
        """
        Night Routine
        - stop radio
          - stop radio
          - disconnect speaker
        - turn off geyser
          - turn off heating
          - disconnect geyser
        - turn off light
          - turn off light
          - disconnect light
        - clean toilet
          - connect toilet
          - flush toilet
          - disconnect toilet
        """
        await self.runner.parallel(
          self.runner.sequential(
            self.speaker.stop_radio(),
            self.speaker.disconnect(),
          ),
          self.runner.sequential(
            self.geyser.stop_heating(),
            self.geyser.disconnect(),
          ),
          self.runner.sequential(
            self.light.turn_off(),
            self.light.disconnect(),
          ),
          self.runner.sequential(
            self.toilet.connect(),
            self.toilet.flush_toilet(),
            self.toilet.clean_toilet(),
            self.toilet.disconnect(),
          )
        )


async def main():
    routine = Routine(
      device_factory=DeviceFactory,
      runner=Runner
    )
    await routine.morning_routine()
    await routine.night_routine()

if __name__ == '__main__':
    asyncio.run(main())
