proceeds = input("Enter proceeds -> ")
outgoings = input("Enter outgoings -> ")

try:
    proceeds = float(proceeds)
    outgoings = float(outgoings)
except ValueError:
    print("Inputted values are not numbers")
    exit(1)

if proceeds > outgoings:
    print("You are working with profit")
    print(f"Ratio proceeds/outgoings = {proceeds/outgoings:.2f}")

    staff = input("Enter quantity staff -> ")
    try:
        staff = int(staff)
    except ValueError:
        print("Inputted value are not integer")
        exit(1)

    print(f"Profit in one employee: {(proceeds - outgoings) / staff:.2f}")
elif proceeds < outgoings:
    print("You are working with loss")
else:
    print("You are working in zero")
