#!/usr/bin/python3
"""
This module contains the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Attributes:
        obj (object): The object to be checked
        a_class (Class): The class the object is supossed to belong

    Return: True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.
    """
    return (isinstance(obj, a_class))
