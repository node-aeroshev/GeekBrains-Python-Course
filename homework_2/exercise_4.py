some_string = input("Enter any string -> ")

for num, word in enumerate(some_string.split(' ')[:10]):
    print(f"{num}: {word}")
