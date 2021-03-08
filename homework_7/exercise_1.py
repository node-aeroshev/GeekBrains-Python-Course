from typing import Any, List
from copy import deepcopy


class Matrix:
    """Класс матрицы"""

    def __init__(self, list_of_lists: List[List[Any]]) -> None:
        self._matrix = list_of_lists
        self.height = len(list_of_lists)
        self.width = len(list_of_lists[0])

    def __str__(self) -> str:
        result_string = ''
        for row in self._matrix:
            for column in row:
                result_string += f"{column} "
            result_string += '\n'
        return result_string

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if isinstance(other, Matrix):
            if not (self.height == other.height and self.width == other.width):
                raise TypeError('Not equal size matrix')
        else:
            raise TypeError('Incompatible types')

        result_matrix = deepcopy(self)

        for row_i in range(self.height):
            for column_i in range(self.width):
                result_matrix._matrix[row_i][column_i] = \
                    self._matrix[row_i][column_i] + other._matrix[row_i][column_i]

        return result_matrix


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    matrix_2 = Matrix([[10, 11, 12],
                       [20, 25, 34],
                       [89, 23, 204]])

    matrix_3 = Matrix([[34, 45, 34, 76, 56],
                      [23, 51, 34, 89, 1]])

    matrix_4 = Matrix([[12432, 4354, 464, 5673, 5],
                      [454, 234, 12, 67, 4]])

    print(f"Matrix 1\n{matrix_1}")
    print(f"Matrix 2\n{matrix_2}")
    print(f"Matrix 3\n{matrix_3}")
    print(f"Matrix 4\n{matrix_4}")

    print(f"Matrix 1 + Matrix 2\n{matrix_1 + matrix_2}")

    print(f"Matrix 1\n{matrix_1}")
    print(f"Matrix 2\n{matrix_2}")

    print(f"Matrix 3 + Matrix 4\n{matrix_3 + matrix_4}")

    try:
        matrix_except = matrix_1 + matrix_3
    except TypeError as err:
        print("Error occurred:", err)

    try:
        matrix_except = matrix_1 + 4
    except TypeError as err:
        print("Error occurred:", err)
