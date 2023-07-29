from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude) -> None:
        self.latitude: float = radians(latitude)
        self.longitude: float = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other) -> float:
        cos_d: float = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
            self.longitude - other.longitude)
        return 6371 * acos(cos_d)
