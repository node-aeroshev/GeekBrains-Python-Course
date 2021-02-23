from typing import List


def user_input() -> List[str]:
    input_string = ' '
    list_strings = []
    while input_string != '':
        input_string = input("-> ")
        list_strings.append(input_string)

    return list_strings


if __name__ == '__main__':
    _data = user_input()
    with open("exercise_1.txt", "w") as file:
        for string in _data:
            print(string, file=file)
