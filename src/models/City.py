from models.Point import Point


class City(Point):
    def __init__(self, latitude, longitude, name, population) -> None:
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def info(self) -> None:
        print(f"City {self.name}, population {self.population}.")
