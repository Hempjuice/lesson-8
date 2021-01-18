from dataclasses import dataclass
from basevehicle import BaseVehicle


@dataclass
class Boat(BaseVehicle):
    type_name: str = 'Яхта'

    def start_moving(self):
        super().start_moving()
