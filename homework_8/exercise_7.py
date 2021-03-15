from copy import copy


class NotComplexNumberError(Exception):
    ...


class ComplexNumber:
    def __init__(self, real: int, imaginary: int) -> None:
        self._real = real
        self._imaginary = imaginary

    def __str__(self) -> str:
        return f"{self._real} + i{self._imaginary}"

    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        if isinstance(other, ComplexNumber):
            result = copy(self)
            result._real = self._real + other._real
            result._imaginary = self._imaginary + other._imaginary
            return result
        else:
            raise NotComplexNumberError("Try add with not complex number")

    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        if isinstance(other, ComplexNumber):
            result = copy(self)
            result._real = self._real * other._real - self._imaginary * other._imaginary
            result._imaginary = self._real * other._imaginary + other._real * self._imaginary
            return result
        else:
            raise NotComplexNumberError("Try multiply with not complex number")


if __name__ == '__main__':
    cn_1 = ComplexNumber(2, 1)
    cn_2 = ComplexNumber(3, 4)

    print(f"({cn_1}) * ({cn_2}) = {cn_1 * cn_2}")
    print(f"({cn_1}) + ({cn_2}) = {cn_1 + cn_2}")
    print(cn_1)
    print(cn_2)

    try:
        res_exp = cn_1 + 1
    except NotComplexNumberError as err:
        print("Handling error:", err)
    try:
        res_exp = cn_2 * 4
    except NotComplexNumberError as err:
        print("Handling error:", err)
