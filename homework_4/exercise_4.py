from typing import List, Generator

source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# Генератор
def no_repeat(source: List[int]) -> Generator[int, None, None]:
    for item in source:
        if source.count(item) == 1:
            yield item


# List comprehension
target_list = [item
               for item in source_list
               if source_list.count(item) == 1]


if __name__ == '__main__':
    result = []
    for item in no_repeat(source_list):
        result.append(item)

    print("Generator: ", result)
    print("List comprehension: ", target_list)
