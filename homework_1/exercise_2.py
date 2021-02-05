time_ = input("Enter time in seconds: ")

time_integer = 0
try:
    time_integer = int(time_)
except ValueError:
    print("You enter not a number")
    exit(1)

hours = time_integer // 3600
if hours // 24 > 0:
    hours = hours % 24
time_integer = time_integer % 3600
minutes = time_integer // 60
seconds = time_integer % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
