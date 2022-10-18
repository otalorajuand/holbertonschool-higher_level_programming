#!/usr/bin/python3
"""
This module includes the class Base which handles
the id for other classes.
"""
import json


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
