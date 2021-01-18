from dataclasses import dataclass
from basevehicle import BaseVehicle


@dataclass
class Car(BaseVehicle):
    type_name: str = 'Автомобиль'

    def start_moving(self):
        if self._has_fuel:
            super().start_moving()
        else:
            raise ValueError(self.full_name + ': бак пуст! Нужно заправиться')

    def refuel(self):
        if self._has_fuel:
            raise ValueError(self.full_name + ' уже заправлен!')
        else:
            self._has_fuel = True
            print(self.full_name + ' заправлен')
