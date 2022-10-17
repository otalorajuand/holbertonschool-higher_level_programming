#!/usr/bin/python3
"""
This module includes the class Base which handles 
the id for other classes.
"""


class Base:
    """This class handles the instance attribute id for other 
    classes to save code

    Attributes:
        __nb_objects (int): a counter for the number of objects created
        from this class
        id (int): the id the user wants to assign to the objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
