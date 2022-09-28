#!/usr/bin/python3
"""square class"""


class Square:
    """defines a square

        Attributes:
        size (int): The size of a side of the square.
    """
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
