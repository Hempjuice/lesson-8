from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseVehicle:
    __metaclass__ = ABCMeta
    name: str
    _color: str = None
    type_name: str = None
    _is_moving: bool = False
    _has_fuel: bool = False

    @abstractmethod
    def start_moving(self):
        if self._is_moving:
            raise ValueError(self.full_name + ' уже движется!')
        else:
            self._is_moving = True
            print(self.full_name + ' начинает движение')

    def stop_moving(self):
        if self._is_moving:
            self._is_moving = False
            print(self.full_name + ' останавливается...')
        else:
            raise ValueError(self.full_name + ' уже стоит!')

    @property
    def full_name(self):
        res = self.type_name

        if self.color is not None:
            res = self.color + ' ' + res

        return res.capitalize() + ' "' + self.name + '"'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        try:
            self._color = str(val)
        except Exception:
            print(f'Неверное значение цвета: {val}')
