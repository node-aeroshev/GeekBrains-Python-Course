class Stationery:
    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> str:
        return f"Запуск отрисовки {self.title}"


class Pencil(Stationery):
    def draw(self) -> str:
        return f"Рисую {self.title}"


class Pen(Stationery):
    def draw(self) -> str:
        return f"Пишу {self.title}"


class Handle(Stationery):
    def draw(self) -> str:
        return f"Выделяю {self.title}"


if __name__ == '__main__':
    stationery = Stationery("Канцелярия")
    pencil = Pencil("Красный карандаш")
    pen = Pen("Синяя ручка")
    handle = Handle("Жёлтый маркер")

    print(stationery.draw())
    print(pencil.draw())
    print(pen.draw())
    print(handle.draw())
