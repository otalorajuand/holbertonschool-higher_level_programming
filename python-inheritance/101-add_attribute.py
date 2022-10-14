#!/usr/bin/python3
"""
This module contains the function add_attribute
"""


def add_attribute(cls, attr_name, attr_value):
    """ This functions adds an attribute to an instances, if possible.

    Attributes:
        cls (object): An instance of a class
        attr_name (str): The name of the new attribute
        attr_value: The value of the new attribute.
    """

    if '__dict__' not in dir(cls):
        raise TypeError("can't add new attribute")

    cls.__dict__[attr_name] = attr_value
