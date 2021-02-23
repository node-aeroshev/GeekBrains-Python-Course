from random import randrange


Q_NUM = 10

if __name__ == '__main__':
    with open("exercise_5.txt", "w+") as file:
        for _ in range(Q_NUM):
            _num = randrange(100)
            file.write(f"{_num} ")

        file.seek(0)

        line_num = file.read()
        list_num = [int(item) for item in line_num.split(' ')[:-1]]
        print(f"Sum - {sum(list_num)}")
