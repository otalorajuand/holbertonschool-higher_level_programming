#!/usr/bin/python3
"""
This module contains the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square and inherits from Rectangle.

    Attributes:
        width (int): the size of the square
        height (int): the size of the square
        x (int): the x coordinate of the square
        y (int): the y coordinate of the square
        id (int): An identifier of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute

        Attributes:
            args (list): containts the attributes to be updated in the
            following order:

            1st argument should be the id attribute
            2nd argument should be the size attribute
            3th argument should be the x attribute
            4th argument should be the y attribute

            kwargs (dict): A dictionary with the name of the attrs
            as keys and the values to change associated.
            """

        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            elif count == 1:
                self.size = arg
            elif count == 2:
                self.x = arg
            elif count == 3:
                self.y = arg
            count += 1

        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}" \
               f" - {self.width}"


