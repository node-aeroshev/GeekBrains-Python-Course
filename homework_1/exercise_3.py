user_input = input("Enter random number -> ")

number = 0
try:
    number = int(user_input)
except ValueError as err:
    print(f"You enter not a number: err -> {err}")
    exit(1)

single_number = number
double_number = int(user_input * 2)
triple_number = int(user_input * 3)

print(f"Single: {single_number}, double: {double_number}, triple: {triple_number}")

print(f"Result n + nn + nnn = {single_number + double_number + triple_number}")
