#!/usr/bin/python3
"""
This module contains the class BaseGeomtry
"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Checks for value

        Attributes:
            name: The name of the attribute
            value: The value of the attribute"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
