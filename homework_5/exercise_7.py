import json
from typing import Any, List, Dict


def read_file_data(filename: str) -> List[str]:
    with open(filename, "r") as file:
        _data = file.readlines()
    return _data


def write_to_json(filename: str, _data: List[Any]) -> None:
    with open(filename, "w") as file:
        json.dump(_data, file)


def count_profit(_companies: List[str]) -> Dict[str, int]:
    stat_companies = dict()  # type: Dict[str, int]
    for company in _companies:
        name, _, income, expense = company.split(' ')
        try:
            income = int(income)
            expense = int(expense)
        except ValueError:
            continue
        stat_companies = stat_companies | {
            name: income - expense
        }
    return stat_companies


def count_average_profit(stat_companies: Dict[str, int]) -> Dict[str, float]:
    _average_profit = []
    for _, profit in stat_companies.items():
        if profit > 0:
            _average_profit.append(profit)

    return {
        "average_profit": sum(_average_profit) / len(_average_profit)
    }


if __name__ == '__main__':
    list_of_companies = read_file_data("exercise_7.txt")
    companies = count_profit(list_of_companies)
    average_profit = count_average_profit(companies)
    write_to_json("exercise_7.json", [companies, average_profit])
