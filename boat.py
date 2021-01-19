from dataclasses import dataclass
from basevehicle import BaseVehicle


@dataclass
class Boat(BaseVehicle):
    type_name: str = 'Яхта'

    def start_moving(self):
        if self._is_moving:
            raise ValueError(self.full_name + ' уже движется!')
        else:
            self._is_moving = True
            print(self.full_name + ' начинает движение')
