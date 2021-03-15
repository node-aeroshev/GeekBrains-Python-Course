from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def tissue(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return 'Abstract clothes class'


class Coat(Clothes):
    def __init__(self, name: str, size: float) -> None:
        super().__init__(name)
        self.size = size

    @property
    def tissue(self) -> float:
        return round(self.size / 6.5 + 0.5, 2)

    def __str__(self) -> str:
        return f"Coat {self.name} with size {self.size}"


class Suit(Clothes):
    def __init__(self, name: str, height: float) -> None:
        super().__init__(name)
        self.height = height

    @property
    def tissue(self) -> float:
        return round(2 * self.height + 0.3, 2)

    def __str__(self) -> str:
        return f"Suit {self.name} with height {self.height}"


if __name__ == '__main__':
    try:
        clothes = Clothes('some')
    except TypeError as err:
        print("Error occurred:", err)

    coat = Coat('brown', 47)
    suit = Suit('smoking', 180)

    print(coat)
    print(suit)

    print("Tissue for coat ->", coat.tissue)
    print("Tissue for suit ->", suit.tissue)
