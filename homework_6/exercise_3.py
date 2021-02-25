class Worker:
    def __init__(self,
                 name: str,
                 surname: str,
                 position: str,
                 wage: float,
                 bonus: float) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self) -> str:
        return ' '.join([self.name, self.surname])

    def get_total_income(self) -> float:
        return self._income["wage"] + self._income["bonus"]


if __name__ == '__main__':
    manager = Position("Will", "Smit", "artist", 5001.0, 4020.45)
    print("Full name", manager.get_full_name())
    print("Income", manager.get_total_income())
    print("Nooooo, this protected", manager._income)

    pos = Position("John", "Lebovski", "no working", 200, 0)
    print("Full name", pos.get_full_name())
    print("Income", pos.get_total_income())
    print("Position", pos.position)
