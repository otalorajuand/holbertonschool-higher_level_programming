#!/usr/bin/python3
"""square class"""


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

    def my_print(self):
        """prints in stdout the square with the character #"""

        if not self.size:
            print()

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
                if j == self.size - 1:
                    print()
