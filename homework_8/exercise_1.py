import re
from copy import copy
from typing import Tuple


class Date:
    """
    Класс даты получаемый из строки
    правильного формата DD-MM-YYYY
    """
    pattern = r'([\s]*[\d]{1,2}[-][\d]{1,2}[-][\d]{4}[\s]*){1}'

    def __init__(self, date: str) -> None:
        self.day, self.month, self.year = self._validate_date(
            *self._cast_to_num(
                *self._parse_date(date)
            )
        )

    @classmethod
    def _parse_date(cls, string_date: str) -> Tuple[str, str, str]:
        match = re.search(cls.pattern, string_date)
        if match:
            result = match.group(0)
            day, month, year = result.strip(' ').split('-')
            return day, month, year
        else:
            raise TypeError('Error parse')

    @staticmethod
    def _cast_to_num(day: str, month: str, year: str) -> Tuple[int, int, int]:
        cast_day = copy(day)
        cast_month = copy(month)
        cast_year = copy(year)
        return int(cast_day), int(cast_month), int(cast_year)

    @staticmethod
    def _validate_date(day: int, month: int, year: int) -> Tuple[int, int, int]:
        if day not in range(1, 32):
            raise TypeError("Day can be only 1 - 31")
        if month not in range(1, 12):
            raise TypeError("Month can be only 1 - 12")
        if not year > 0:
            raise TypeError("Year must be positive")

        return day, month, year

    def __str__(self) -> str:
        return f"Day: {self.day}, Month: {self.month}, Year: {self.year}"

    def __eq__(self, other: 'Date') -> bool:
        return self.day == other.day and \
               self.month == other.month and \
               self.year == other.year

    def __mul__(self, other):
        ...

    def __truediv__(self, other):
        ...


if __name__ == '__main__':
    date_now = Date('   07-04-2021  ')
    print(date_now)
    try:
        date_except = Date('32-04-2021')
    except TypeError as err:
        print("Error occurred:", err)
    try:
        date_except = Date('234_345_2021')
    except TypeError as err:
        print("Error occurred:", err)
    try:
        date_except = Date('23-34-2021')
    except TypeError as err:
        print("Error occurred:", err)
    try:
        date_except = Date('23-11--2021')
    except TypeError as err:
        print("Error occurred:", err)
    try:
        date_except = Date('str-str-str')
    except TypeError as err:
        print("Error occurred:", err)

    date_double = Date('    01-01-2021      02-02-2021')
    print(date_double)
    date_triple = Date('    01-01-2021      02-02-2021     03-03-2021')
    print(date_triple)
