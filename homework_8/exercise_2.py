class GlideZeroDivisionError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise self
        return a / b


if __name__ == '__main__':
    handler_err = GlideZeroDivisionError("division by zero")
    try:
        res = handler_err.div(10, 0)
    except GlideZeroDivisionError as err:
        print("Handling error:", err)
    else:
        print("Res divided 10 / 0 =", res)

    try:
        res = handler_err.div(10, 2)
    except GlideZeroDivisionError as err:
        print("Handling error:", err)
    else:
        print("Res divided 10 / 2 =", res)
