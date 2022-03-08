from typing import TypeVar


Self = TypeVar("Self")


class Vehicle:
    def __init__(self, registration_number: str) -> None:
        self.registration_number = registration_number
    
    def get_registration_number(self) -> str:
        return self.registration_number

class AccessPoint:
    def __init__(self, booth_id, executive_id) -> None:
        self.booth_id = booth_id
        self.executive_id = executive_id


class EntryPoint(AccessPoint):
    INSTANCE = None
    
    def __init__(self, booth_id, executive_id) -> None:
        print('triggered init', self, self.__dict__)
        super().__init__(booth_id, executive_id)
    
    @classmethod
    def get_instance(cls, booth_id, executive_id):
        return cls(booth_id, executive_id)

class Parking:
    data_store = {}     # registration_number -> ticket_id mapping


ep = EntryPoint.get_instance(booth_id='ne01', executive_id='001451')
ep2 = EntryPoint.get_instance(booth_id='ne02', executive_id='001452')