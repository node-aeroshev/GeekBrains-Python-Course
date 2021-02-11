from typing import List, Tuple, Dict


goods = []  # type: List[Tuple[int, dict]]

analytics = {
    "name": [],
    "price": [],
    "quantity": [],
    "measure": []
}  # type: Dict[str, list]

mark = 1
while True:
    stop_word = input("Stop execute? Any word or just enter to continue -> ")

    if stop_word != '':
        break

    name = input("Enter a name of product -> ")
    price = input("Enter a price of product -> ")
    quantity = input("Enter a quantity of product -> ")
    measure = input("Enter a type of measure -> ")

    goods.append(
        tuple(
            (mark, {
                "name": name,
                "price": price,
                "quantity": quantity,
                "measure": measure
            })
        )
    )
    mark += 1

for item in goods:
    for key in analytics.keys():
        if item[1][key] not in analytics[key]:
            analytics[key].append(item[1][key])

print(f"Goods:\n{goods}")
print(f"Analytics:\n{analytics}")
