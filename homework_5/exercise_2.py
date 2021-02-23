from typing import List, Tuple


def _count_lines(ls_ln: List[str]) -> Tuple[int, List[int]]:
    count_lines = len(ls_ln)
    count_words = []
    for line in ls_ln:
        count_words.append(len(line.split(' ')))

    return count_lines, count_words


if __name__ == '__main__':
    with open("exercise_2.txt", "r") as file:
        list_of_lines = file.readlines()
        c_lines, c_words = _count_lines(list_of_lines)

    if c_lines and c_words:
        print(f"Lines: {c_lines}\nWords: {c_words}")
