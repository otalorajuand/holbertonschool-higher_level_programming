#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle and inherits from Base.

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): the x coordinate of the rectangle
        y (int): the y coordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
