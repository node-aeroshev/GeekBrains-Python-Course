from abc import ABC, abstractmethod


class Warehouse:
    ...


class OfficeEquipment(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Office + {self.name}"


class Printer(OfficeEquipment):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Scanner(OfficeEquipment):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Copier(OfficeEquipment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

