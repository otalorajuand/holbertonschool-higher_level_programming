#!/usr/bin/python3
from functools import total_ordering
"""square class"""


@total_ordering
class Square:
    """defines a square

        Attributes:
        size (int): The size of a side of the square.
    """
    def __init__(self, size=0):
        """initializes the object"""
        self.size = size

    @property
    def size(self):
        """object getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """object setter"""
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the area of the square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """equal method"""
        if self.size == other.size:
            return (True)
        return (False)

    def __lt__(self, other):
        """lower than method"""
        if self.size < other.size:
            return (True)
        return (False)
