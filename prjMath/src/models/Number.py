class Number:
    def __init__(self, num: int) -> None:
        self.num = num

    def is_odd(self) -> bool:
        return self.num % 2 != 0
