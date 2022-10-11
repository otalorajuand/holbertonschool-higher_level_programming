#!/usr/bin/python3
"""
This module contains the class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a rectangle
    Attributes:
        size: The size of a side of the square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
