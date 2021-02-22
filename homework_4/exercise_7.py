from typing import Generator
from functools import reduce


def fact(n: int) -> Generator[int, None, None]:
    sequence_fact = []
    for _num in range(1, n + 1):
        sequence_fact.append(_num)
        yield reduce(lambda prev_el, el: prev_el * el, sequence_fact)


if __name__ == '__main__':
    for res in fact(5):
        print(res)
