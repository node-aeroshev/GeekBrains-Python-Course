month_number = input("Enter number of month -> ")

try:
    month_number = int(month_number)
except ValueError as err:
    print(f"This is not a number: err -> {err}")
    exit(1)

if month_number < 1 or month_number > 12:
    print("Outside 1 - 12")
    exit(1)

decision = {
    frozenset({1, 2, 12}): 'Winter',
    frozenset({3, 4, 5}): 'Spring',
    frozenset({6, 7, 8}): 'Summer',
    frozenset({9, 10, 11}): 'Fall'
}

decision_list = [
    [1, 2, 12, "Winter"],
    [3, 4, 5, "Spring"],
    [6, 7, 8, "Summer"],
    [9, 10, 11, "Fall"]
]

print("Dict example")
for key, value in decision.items():
    if month_number in key:
        print(value)

print("List example")
for item in decision_list:
    if month_number in item:
        print(item[-1])
