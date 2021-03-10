from abc import ABC, abstractmethod


class FullWarehouseError(Exception):
    ...


class NotFoundFacilitiesError(Exception):
    ...


class OfficeEquipment(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Office + {self.name}"

    @abstractmethod
    def work(self, task: str) -> str:
        ...


class Printer(OfficeEquipment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def work(self, task: str) -> str:
        return f"Print {str}"


class Scanner(OfficeEquipment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def work(self, task: str) -> str:
        return f"Scan {task}"


class Copier(OfficeEquipment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def work(self, task: str) -> str:
        return f"Copy {task}"


class Warehouse:
    def __init__(self, size: int = 10) -> None:
        self._current_size = 0
        self.size = size
        self._facilities = []

    def put_item(self, item: OfficeEquipment) -> None:
        if self._current_size < self.size:
            self._facilities.append(item)
            self._current_size += 1
        else:
            raise FullWarehouseError("Warehouse is full")

    def get_item(self, name: str) -> OfficeEquipment:
        for item in self._facilities:
            if item.name == name:
                return item
        raise NotFoundFacilitiesError(f"Not found facilities with name {name}")


