from typing import List
from copy import copy


class NonIntegerError(Exception):
    def __init__(self, message: str, stop_word: str) -> None:
        self.message = message
        self._stop = stop_word
        self._clear_list = []

    def flush(self) -> None:
        self._clear_list = []

    def check_only_digit(self, controlled_list: List[str]) -> None:
        for item in controlled_list:
            if item == self._stop:
                raise self
            if not item.isdigit():
                continue
            self._clear_list.append(int(item))

    def get_clear_list(self) -> List[int]:
        return copy(self._clear_list)


def cli(handler_cleaner: NonIntegerError) -> List[int]:
    while True:
        user_input = input("Enter values or say stop -> ")
        raw_list = user_input.split(' ')
        try:
            handler_cleaner.check_only_digit(raw_list)
        except NonIntegerError as err:
            print(err.message)
            break
    return handler_cleaner.get_clear_list()


if __name__ == '__main__':
    handler = NonIntegerError("Entered stop word", "stop")
    clear_list = cli(handler)
    print("Clear list: ", clear_list)
