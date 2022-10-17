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
        if type(value) != int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        result_string = ""
        for j in range(self.y):
            result_string += "\n"
        for i in range(self.height):
            result_string += (" " * self.x) + ("#" * self.width) + "\n"
        print(result_string[:-1])

    def __str__(self):
        """returns the string version of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
               f" - {self.width}/{self.height}"

    def update(self, *args):

        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            elif count == 1:
                self.width = arg
            elif count == 2:
                self.height = arg
            elif count == 3:
                self.x = arg
            elif count == 4:
                self.y = arg
            count += 1
