class Bird:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def info(self):
        print(f'{self.name} носит одежду размера «{self.size}».')


# implementation
bird_1 = Bird("bob", 10)
bird_1.info()
