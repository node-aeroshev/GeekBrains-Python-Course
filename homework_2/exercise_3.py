# TODO
month_number = input("Enter number of month -> ")

try:
    month_number = int(month_number)
except ValueError:
    print("This's a number")
    exit(1)

if month_number < 1 or month_number > 12:
    print("Outside 1 - 12")
    exit(1)

decision = {
    (1, 2, 12): 'Winter',
    (3, 4, 5): 'Spring',
    (6, 7, 8): 'Summer',
    (9, 10, 11): 'Fall'
}

decision_list = [
    [1, 2, 12],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]

for key, value in decision.items():
    if month_number in key:
        print(value)
