

34 * 45  # multiplication is denoted by *
57 / 2  # division is denoted by /
57 // 2  # floor division- it discards the fractional part
57 % 2  # returns the remainder from the division
3 ** 2  # 3 raised to the power of 2
round(100/3, 2)  # round the result to 2 places
(100 - 5 * 3) / 5  # order of operations works as expected


class Calculate:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def get_nums(self):
        ...

    def add(self) -> float:
        """addition
        """
        return self.num1 + self.num2

    def subtract(self):
        # subtraction
        return self.num1 - self.num2
