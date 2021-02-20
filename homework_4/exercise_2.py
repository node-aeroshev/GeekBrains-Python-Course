from typing import List, Generator


def small_left(source: List[int]) -> Generator[int, None, None]:
    for curr in range(1, len(source)):
        if source[curr - 1] < source[curr]:
            yield source[curr]


source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

if __name__ == '__main__':
    big_list = []
    for big in small_left(source_list):
        big_list.append(big)
    print(big_list)
