"""
При выполненни этого задания возникло два вопроса
1. Прокидывать параметры надо в __init__ или __new__?
2. Насколько легально валидировать параметры при инициализации?
"""


class Road:
    def __init__(self,
                 length: float = 0.0,
                 width: float = 0.0) -> None:
        self.__length = self._validate_measure(length)
        self.__width = self._validate_measure(width)

    # def __new__(cls, *args, **kwargs):
    #     """
    #     Или именно при создании прокидывать параметры?
    #     """
    #     pass

    @staticmethod
    def _validate_measure(measure: float) -> float:
        """
        Насколько легально проводить вадидацию при инициализации экземпляра?
        """
        if measure < 0.0:
            return 0.0
        return measure

    def weight(self, weight_per: float, depth: float) -> float:
        return self.__length * self.__width * weight_per * depth


if __name__ == '__main__':
    road = Road(length=5000, width=20)
    weight = road.weight(weight_per=25, depth=5)
    print("Weight road", weight, "kg")
