"""
Exercise 4
"""


def my_func_1(x: int, y: int) -> float:
    return x**y


def my_func_2(x: int, y: int) -> float:
    res = 1
    if y > 0:
        for _ in range(y):
            res *= x
    elif y < 0:
        for _ in range(abs(y)):
            res /= x
    return res


# Test case
print("my_func_1")
print(my_func_1(5, -2))
print(my_func_1(5, 0))
print(my_func_1(5, 2))

print("my_func_2")
print(my_func_2(5, -2))
print(my_func_2(5, 0))
print(my_func_2(5, 2))
