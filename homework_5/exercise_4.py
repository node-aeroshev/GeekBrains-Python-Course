vocabulary = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}


if __name__ == '__main__':
    with open("exercise_4.txt", "r") as input_f, open("exercise_4_translate.txt", "w") as output_f:
        for line in input_f:
            word, _, digit = line.split(' ')
            output_f.write(f"{vocabulary[word]} - {digit}")
