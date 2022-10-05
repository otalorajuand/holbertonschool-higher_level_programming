#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """Definition of class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * self.width + 2 * self.height)

    def __str__(self):
        """print method"""
        result_string = ""

        if not self.height or not self.width:
            return (result_string)

        for i in range(self.height):
            result_string += ("#" * self.width) + "\n"
        return (result_string[:-1])

    def __repr__(self):
        """string representation of object"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
