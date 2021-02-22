from typing import Generator, Iterable, Any
from itertools import count, cycle


def _count(start: int, stop: int, step: int = 1, ) -> Generator[int, None, None]:
    for _num in count(start=start, step=step):
        if _num == stop:
            break
        yield _num


def _cycle(iterable: Iterable, count_loops: int) -> Generator[Any, None, None]:
    _loops = 0
    _len_iterable = len(iterable)
    for _el in cycle(iterable):
        if _loops == (count_loops * _len_iterable):
            break
        yield _el
        _loops += 1


if __name__ == '__main__':
    print("Custom count()")
    for num in _count(1, 10):
        print(num)

    print("Custom cycle()")
    for el in _cycle([ValueError, None, 1, 'str', 2.5], 4):
        print(el)
