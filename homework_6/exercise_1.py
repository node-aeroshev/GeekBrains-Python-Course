"""
По моей реализации неверной работы быть не может)
Сначала содержится более сложная реализация, для
развития владения различными инструментамии.
Далее следует более простая реализация, которая скорее всего
лучше соответвует условию задания.
"""
from time import sleep, time
from typing import Optional
from itertools import cycle, islice
from functools import partial
from enum import Enum


class TrafficColor(Enum):
    """
    Перечисление цветов светофора
    """
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight:
    """
    Класс светофора
    """
    __slots__ = ('time_life', '__color', '__handler_switch')

    __loop = [
        TrafficColor.RED,
        TrafficColor.YELLOW,
        TrafficColor.GREEN,
        TrafficColor.YELLOW
    ]

    def __init__(self, time_life: int, color_traffic: TrafficColor = TrafficColor.RED) -> None:
        self.time_life = time_life
        self.__color = color_traffic
        self.__handler_switch = {
            TrafficColor.RED: partial(sleep, 7),
            TrafficColor.YELLOW: partial(sleep, 2),
            TrafficColor.GREEN: partial(sleep, 5)
        }

    def running(self) -> None:
        """
        Переключение светофора
        :return: None
        """
        start = time()
        for light in islice(cycle(self.__loop), self.__loop.index(self.__color), None):
            end = time()
            if end - start > self.time_life:
                break

            print("Light now", light)
            self.__handler_switch[light]()


class SimpleTrafficLight:
    """
    Простой класс светофора
    """
    __slots__ = ('__color', '__handler_switch')

    __chain_switch = {
        'red': 'yellow',
        'green': None,
        'yellow': 'green'
    }

    def __init__(self, color_traffic: str = 'red') -> None:
        self.__color = color_traffic
        self.__handler_switch = {
            'red': partial(sleep, 7),
            'yellow': partial(sleep, 2),
            'green': partial(sleep, 5)
        }

    def running(self, next_color: Optional[str] = None) -> None:
        print("Light now", self.__color)
        self.__handler_switch[self.__color]()
        if self.__chain_switch[self.__color] == next_color:
            self.__color = self.__chain_switch[self.__color]
        else:
            raise RuntimeError


if __name__ == '__main__':
    crossroad = TrafficLight(20, TrafficColor.YELLOW)
    crossroad.running()

    simple_crossroad = SimpleTrafficLight()
    simple_crossroad.running('yellow')
    simple_crossroad.running('green')
    simple_crossroad.running()

    simple_crossroad = SimpleTrafficLight('yellow')
    simple_crossroad.running('red')
