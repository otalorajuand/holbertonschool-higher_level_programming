#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """
        checks if instace

        attributes:
            obj (object): The object to check.
            a_class (Class): The class it is supossed to belong.

        returns: eturns True if the object is exactly an instance
        of the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
