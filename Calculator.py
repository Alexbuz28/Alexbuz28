class Calculator:
    def __init__(self):
        pass

    def __add__(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtruct(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            return x1 / x2

        if 0 == x2:
            print("Деление на 0 нельзя!")
        else:
            return x1 / x2
