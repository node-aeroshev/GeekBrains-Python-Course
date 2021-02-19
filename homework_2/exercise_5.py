from typing import List


list_of_rating = []  # type: List[int]

while True:
    rating = input("Enter a rating, for stop say 'stop' -> ")
    if rating == 'stop':
        break

    try:
        rating = int(rating)
    except ValueError as err:
        print("Catch error: ", err)
        exit(1)

    count_ = list_of_rating.count(rating)
    index_ = 0
    try:
        st = list_of_rating.index(rating)
        index_ = st + count_
    except ValueError as err:
        index_ = 0
        for item in list_of_rating:
            if rating <= item:
                index_ += 1

    list_of_rating.insert(index_, rating)

    print(list_of_rating)
