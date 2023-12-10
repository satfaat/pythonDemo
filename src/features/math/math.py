

from src.features.debug.debug import LOGGER


def area(width, height):
    # area is width multiplied by height
    area = width * height
    LOGGER.info(f'Area is {area}')
    return area
