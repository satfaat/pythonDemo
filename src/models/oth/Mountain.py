from models.math.Point import Point


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height) -> None:
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def info(self) -> None:
        print(f"Высота горы {self.name} - {self.height} м.")
