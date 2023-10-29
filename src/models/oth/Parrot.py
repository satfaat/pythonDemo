from models.oth.Bird import Bird


class Parrot(Bird):
    def __init__(self, name, size, sound) -> None:
        super().__init__(name, size)
        self.sound = sound

    def info(self) -> None:
        print(f'{self.name} носит одежду размера «{self.size}» и {self.sound}.')
