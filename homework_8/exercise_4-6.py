from abc import ABC, abstractmethod
from typing import Any


class FullWarehouseError(Exception):
    ...


class NotFoundFacilitiesError(Exception):
    ...


class ItemIncompatibleError(Exception):
    ...


class OfficeEquipment(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Office + {self.name}"

    @classmethod
    def tuning(cls, field: str, value: Any) -> None:
        setattr(cls, field, value)

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

    def __str__(self) -> str:
        return f"Warehouse size = {self.size}"

    @staticmethod
    def _validate_object(item: OfficeEquipment) -> bool:
        if issubclass(item.__class__, OfficeEquipment):
            return True
        else:
            raise ItemIncompatibleError("Not valid item")

    def put_item(self, item: OfficeEquipment) -> None:
        if self._validate_object(item):
            if self._current_size < self.size:
                self._facilities.append(item)
                self._current_size += 1
            else:
                raise FullWarehouseError("Warehouse is full")

    def get_item(self, name: str) -> OfficeEquipment:
        for pos, item in enumerate(self._facilities):
            if item.name == name:
                return self._facilities.pop(pos)
        raise NotFoundFacilitiesError(f"Not found facilities with name {name}")

    def get_stat(self) -> dict:
        stat = dict()
        for item in self._facilities:
            if stat.get(item.__class__, None):
                stat[item.__class__] += 1
            else:
                stat[item.__class__] = 1
        return stat


if __name__ == '__main__':
    warehouse = Warehouse()

    warehouse.put_item(Copier("copy_1"))
    warehouse.put_item(Copier("copy_2"))
    warehouse.put_item(Copier("copy_3"))
    warehouse.put_item(Scanner("scanner_1"))
    warehouse.put_item(Scanner("scanner_2"))
    warehouse.put_item(Printer("printer_3"))
    print(warehouse.get_stat())

    print(warehouse.get_item("copy_2"))
    print(warehouse.get_stat())

    try:
        warehouse.put_item(NotFoundFacilitiesError())
    except ItemIncompatibleError as err:
        print("Error occurred:", err)

    try:
        for _ in range(20):
            warehouse.put_item(Printer("printer"))
    except FullWarehouseError as err:
        print("Error occurred:", err)

    try:
        warehouse.get_item("no_name")
    except NotFoundFacilitiesError as err:
        print("Error occurred:", err)

    item = warehouse.get_item("scanner_2")
    item.tuning("new_field", "new_value")
    print(item.new_field)
