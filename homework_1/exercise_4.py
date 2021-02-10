user_input = input("Enter integer number -> ")

number = 0
try:
    number = int(user_input)
except ValueError as err:
    print(f"You enter not a number: err -> {err}")
    exit(1)

max_digit = 0
while number > 0:
    candidate = number % 10
    number = number // 10
    if candidate > max_digit:
        max_digit = candidate

print(f"Max digit in number {user_input}, is {max_digit}")
