first_day = input("Enter first day result -> ")
finish_result = input("Enter finish result -> ")

try:
    first_day = float(first_day)
    finish_result = float(finish_result)
except ValueError as err:
    print(f"Incorrect input value: err -> {err}")
    exit(1)

progress = first_day
days = 1
print(f"{days} day: {progress:.2f}")
while progress < finish_result:
    progress *= 1.1
    days += 1
    print(f"{days} day: {progress:.2f}")

print(f"The result was achieved in {days} days")
