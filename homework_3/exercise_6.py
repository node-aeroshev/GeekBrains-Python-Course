"""
Exercise 6
"""


# First stage
def int_func(word: str) -> str:
    return word.capitalize()


# Second stage
def int_func_2(words: str) -> str:
    res = []
    for word in words.split(' '):
        res.append(int_func(word))
    return ' '.join(res)


if __name__ == '__main__':
    print("First stage")
    print(int_func(input("Input word ")))
    print("Second stage")
    print(int_func_2(input("Input words ")))
