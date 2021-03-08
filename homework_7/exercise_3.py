class Cell:
    """Organic cell"""
    def __init__(self, quantity: float) -> None:
        self.quantity = round(quantity)

    @staticmethod
    def _validate_instance(other: 'Cell') -> bool:
        if isinstance(other, Cell):
            return True
        else:
            raise TypeError('Incompatible types')

    def __add__(self, other: 'Cell') -> 'Cell':
        if self._validate_instance(other):
            return Cell(self.quantity + other.quantity)

    def __sub__(self, other: 'Cell') -> 'Cell':
        if self._validate_instance(other):
            if other.quantity > self.quantity:
                raise TypeError('Right side is bigger than left')
            return Cell(self.quantity - other.quantity)

    def __mul__(self, other: 'Cell') -> 'Cell':
        if self._validate_instance(other):
            return Cell(self.quantity * other.quantity)

    def __truediv__(self, other: 'Cell') -> 'Cell':
        if self._validate_instance(other):
            return Cell(self.quantity // other.quantity)

    def __str__(self) -> str:
        return f"Organic cell with {self.quantity} cells"

    def make_order(self, row_len: int) -> str:
        rows_q = self.quantity // row_len
        others = self.quantity % row_len

        result_string = ''
        for row in range(rows_q):
            result_string += '*' * row_len + '\n'

        if others:
            result_string += '*' * others + '\n'

        return result_string


if __name__ == '__main__':
    cell_1 = Cell(3)
    cell_2 = Cell(5)
    cell_3 = Cell(7.45)

    print("Cell 1:", cell_1)
    print("Cell 2:", cell_2)
    print("Cell 3:", cell_3)

    cell_4 = cell_1 + cell_3
    print("Cell 4 = Cell 1 + Cell 2:", cell_4)

    cell_5 = cell_4 - cell_2
    print("Cell 5 = Cell 4 - Cell 2:", cell_5)

    cell_6 = cell_5 * cell_1
    print("Cell 6 = Cell 5 * Cell 1:", cell_6)

    cell_7 = cell_6 / cell_3
    print("Cell 7 = Cell 6 / Cell 3:", cell_7)

    print(cell_6.make_order(3))
    print(cell_4.make_order(4))
    print(cell_3.make_order(2))
