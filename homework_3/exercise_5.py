"""
Exercise 5
"""
from typing import List


def adder() -> int:
    acc = 0
    stop_word = False

    def accumulate(base: int) -> None:
        nonlocal acc
        acc += base

    def consumer() -> List[int]:
        nonlocal stop_word
        ints = []
        input_string = input()

        for item in input_string.split(' '):
            try:
                int_ = int(item)
                ints.append(int_)
            except ValueError:
                if item == 's' or item == 'stop':
                    stop_word = True
                    break
        return ints

    while not stop_word:
        numbers = consumer()
        for number in numbers:
            accumulate(number)
        print("Current sum: ", acc)

    return acc


if __name__ == '__main__':
    print("Result sum: ", adder())
