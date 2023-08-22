from models.Predator import Predator


class Egg(Predator):
    def info(self) -> None:
        print(
            f'Из яйца вылупится птичка {self.name} размера «{self.size}» с когтями размера {self.claws_size}.')
