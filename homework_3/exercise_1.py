from typing import Optional


def divide(a: float, b: float) -> Optional[float]:
    try:
        res = a / b
    except ZeroDivisionError as err:
        print("Error: ", err)
        res = None
    return res


# Test case
print(divide(2, 3))
print(divide(2, 0))
print(divide(4, 2))
print(divide(1200, 25))
