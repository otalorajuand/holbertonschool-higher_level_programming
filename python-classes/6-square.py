#!/usr/bin/python3
"""square class"""


class Square:
    """defines a square

        Attributes:
        size (int): The size of a side of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """object size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """object size setter"""
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """object position getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """object position setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or not 
                isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.size:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()
