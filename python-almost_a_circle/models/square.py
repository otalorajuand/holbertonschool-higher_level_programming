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

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width} "
