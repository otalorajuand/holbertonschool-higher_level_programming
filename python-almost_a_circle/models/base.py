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
        """Returns the JSON string representation of list_dictionaries

        Attributes:
            list_dictionaries (list): A list with the dictionary
            respresentations of objects"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Attributes:
            list_objs (list): The list with objects"""

        res = []
        if list_objs is not None:
            for elem in list_objs:
                res.append(elem.to_dictionary())
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Attributes:
        json_string (str): a string representing a list of dictionaries.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        res = cls(1, 1)
        res.update(**dictionary)

        return res
