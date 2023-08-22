class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires) -> None:
        """Constructor"""
        # super().__init__()
        self.color = color
        self.doors = doors
        self.tiers = tires

    def brake(self):
        """Stop the caar"""
        return "braking"

    def drive(self):
        """Drive the car"""
        return "i'm driving"
