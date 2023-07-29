import math  # импортируйте библиотеку math


class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        # здесь вычислите площадь поверхности шара
        self.surface_area = 4 * math.pi * radius * radius
        self.average_temp_celcius = temp_celsius
        # здесь переведите температуру в градусы Фаренгейта
        self.average_temp_fahrenheit = temp_celsius * 9 / 5 + 32

    def info(self):
        print(
            f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(
            f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")
