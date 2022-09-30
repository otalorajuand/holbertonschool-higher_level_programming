#!/usr/bin/python3
"""Magic Class"""


class Magic:
    """Defines a magic class

        Attributes:
        radius: The radius of the circle
    """
    def __init__(self, radius=0):
        """Initializes the object"""
        if type(self.radius) is not int or type(self.radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        """Calculates the area of the circle"""
        return ((self.radius ** 2) * math.pi)

    def circunference(self):
        """Calculates the circunference of the circle"""
        return (2 * math.pi * self.radius)
