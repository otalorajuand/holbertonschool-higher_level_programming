#!/usr/bin/python3
"""Magic Class"""
import math


class MagicClass:
    """Defines a magic class

        Attributes:
        radius (int): The radius of the circle
    """

    def __init__(self, radius=0):
        """Initializes the object"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        """Calculates the area of the circle"""
        return ((self.radius ** 2) * math.pi)

    def circumference(self):
        """Calculates the circumference of the circle"""
        return (2 * math.pi * self.radius)
