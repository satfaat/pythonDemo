class Number:
    def __init__(self, num: int = None) -> None:
        self.num = num

    def is_odd(self) -> bool:
        return self.num % 2 != 0

    def is_even(self, i: int) -> bool:
        return i % 2 == 0
