from models.Bird import Bird


class Predator(Bird):
    def __init__(self, name, size, claws_size) -> None:
        super().__init__(name, size)
        self.claws_size = claws_size

    def info(self) -> None:
        print(
            f'{self.name} носит одежду размера «{self.size}» и когти размера {self.claws_size}.')
