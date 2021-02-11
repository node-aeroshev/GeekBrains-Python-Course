"""
Exercise 3
"""


def my_func(a, b, c):
    list_exclude = [a, b, c]
    max_ = max(list_exclude)
    list_exclude.remove(max_)
    max_next = max(list_exclude)
    return max_ + max_next


# Test case
print(my_func(1, 2, 3))
print(my_func(120, 2, 0.5))
