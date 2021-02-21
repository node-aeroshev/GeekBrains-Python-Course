from typing import Generator
from functools import reduce


# Generator
def even(_from: int, _to: int) -> Generator[int, None, None]:
    for _num in range(_from, _to + 1):
        if not _num % 2:
            yield _num


# List comprehension
target_list = [_num for _num in range(100, 1001) if not _num % 2]


if __name__ == '__main__':
    list_even = []
    for num in even(100, 1000):
        list_even.append(num)

    res_gen = reduce(lambda prev, el: prev * el, list_even)
    res_lsch = reduce(lambda prev, el: prev * el, target_list)
    print("Generator: ", res_gen)
    print("List comprehension: ", res_lsch)
    print("Is equal results: ", res_lsch == res_gen)
