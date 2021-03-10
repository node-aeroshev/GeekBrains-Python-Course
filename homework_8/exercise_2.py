# Спросить конкретнее

class GlideZeroDivision(ZeroDivisionError):
    def __init__(self, text: str) -> None:
        super().__init__(text)


if __name__ == '__main__':

