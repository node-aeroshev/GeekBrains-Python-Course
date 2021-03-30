from typing import List, Tuple


def who_get_less(employees: List[str], _less: int) -> Tuple[List[str], float]:
    get_less = []
    _mean = []
    for staff in employees:
        surname, money = staff.split(' ')
        try:
            money = int(money)
        except ValueError as err:
            print("Incorrect value in right line")
            continue
        if money < _less:
            get_less.append(surname)
            _mean.append(money)

    return get_less, round(sum(_mean) / len(_mean), 2)


if __name__ == '__main__':
    with open("exercise_3.txt", "r") as file:
        list_of_lines = file.readlines()
        surnames, mean_income = who_get_less(list_of_lines, 20_000)
        print(f"Who get less 20_000: {surnames}\nMean income: {mean_income}")
