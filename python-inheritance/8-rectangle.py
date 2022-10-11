#!/usr/bin/python3
"""
This module include the class Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle
    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle"""
    def __init__(self, width, height):
        self.integer_validator(self, "width", width)
        self.__width = width

        self.integer_validator(self, "height", height)
        self.__height = height
