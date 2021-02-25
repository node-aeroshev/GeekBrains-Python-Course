from typing import Optional
from abc import abstractmethod


class Car:
    def __init__(self,
                 speed: float,
                 color: str,
                 name: str,
                 is_police: bool) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) -> str:
        return f'{self.color} {self.name} moved'

    def stop(self) -> str:
        return f'{self.color} {self.name} stopped'

    def turn(self, direction: str) -> str:
        return f'{self.color} {self.name} has turned on {direction}'

    @abstractmethod
    def show_speed(self) -> None:
        pass

    def buup(self) -> str:
        if self.is_police:
            return 'Stop your car right now!'
        else:
            return "I can't do this"


class TownCar(Car):
    def show_speed(self) -> Optional[str]:
        if self.speed > 60:
            return f'{self.color} {self.name} exceed speed limit 60 km/h'


class SportCar(Car):
    def show_speed(self) -> str:
        return f'{self.color} {self.name} is sport car. No limit... on the track'


class WorkCar(Car):
    def show_speed(self) -> Optional[str]:
        if self.speed > 40:
            return f'{self.color} {self.name} exceed speed limit 40 km/h'


class PoliceCar(Car):
    def show_speed(self) -> str:
        return f'{self.color} {self.name} is police car. I must catch criminals'


if __name__ == '__main__':
    town_car = TownCar(70, 'grey', 'Hyundai', False)
    sport_car = SportCar(200, 'red', 'Ferrari', False)
    work_car = WorkCar(20, 'black', 'Lada', False)
    police_car = PoliceCar(120, 'blue', 'Skoda', True)

    print("Town car speed", town_car.show_speed())
    print("Sport car speed", sport_car.show_speed())
    print("Work car speed", work_car.show_speed())
    print("Police car speed", police_car.show_speed())

    print("Town car move", town_car.go())
    left = "left"
    print("Town car turned", left, town_car.turn(left))
    print("Town car stopped", town_car.stop())

    print("Police made", police_car.buup())
    print("But sport car can't", sport_car.buup())
