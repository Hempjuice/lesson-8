from dataclasses import dataclass
from basevehicle import BaseVehicle


@dataclass
class Car(BaseVehicle):
    type_name: str = 'Автомобиль'

    def start_moving(self):
        if self._is_moving:
            raise ValueError(self.full_name + ' уже движется!')
        elif self._has_fuel:
            self._is_moving = True
            print(self.full_name + ' начинает движение')
        else:
            raise ValueError(self.full_name + ': бак пуст! Нужно заправиться')

    def refuel(self):
        if self._has_fuel:
            raise ValueError(self.full_name + ' уже заправлен!')
        else:
            self._has_fuel = True
            print(self.full_name + ' заправлен')
