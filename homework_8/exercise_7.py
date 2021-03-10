from copy import deepcopy


class NotComplexNumberError(Exception):
    ...


class ComplexNumber:
    def __init__(self, real: int, imaginary: int) -> None:
        self._real = real
        self._imaginary = imaginary

    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        if isinstance(other, ComplexNumber):
            result = deepcopy(self)
            result._real = self._real + other._real
            result._imaginary = self._imaginary + other._imaginary
            return result
        else:
            raise NotComplexNumberError("Try add with not complex number")

    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        ...
