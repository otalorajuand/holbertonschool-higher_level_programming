#!/usr/bin/python3
"""
This module includes the class Base which handles
the id for other classes.
"""
import json
import os


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
            res = [elem.to_dictionary() for elem in list_objs]
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(res))

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
        """Creates an object of the class cls based on a dicitonary
        with attributes

        Attributes:
            dictionary (dict): The dictionary with the attributes
            of the new object
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            res = cls(1, 1)
        elif cls is Square:
            res = cls(1)

        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances read from a file"""
        file_path = f"{cls.__name__}.json"
        if not os.path.exists(file_path):
            return []
        with open(file_path, encoding="utf-8") as f:
            reading = Base.from_json_string(f.read())
        return [cls.create(**elem) for elem in reading]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv

         Attributes:
            list_objs (list): The list with objects"""
        from models.rectangle import Rectangle
        from models.square import Square

        res = []
        if list_objs is not None:
            res = [elem.to_dictionary() for elem in list_objs]

        with open(f"{cls.__name__}.csv", mode="w", encoding="utf-8") as f:
            for elem in res:
                if cls is Rectangle:
                    s_res = f"{elem['id']},{elem['width']},{elem['height']}," \
                              f"{elem['x']},{elem['y']}\n"
                if cls is Square:
                    s_res = f"{elem['id']},{elem['size']}," \
                            f"{elem['x']},{elem['y']}\n"
                f.write(s_res)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        file_path = f"{cls.__name__}.csv"
        if not os.path.exists(file_path):
            return []
        with open(file_path, encoding="utf-8") as f:
            reading_list = f.readlines()

        res = []
        for line in reading_list:
            line = line.rstrip()
            line_list = line.split(",")

            if len(line_list) == 5:
                dict_obj = {"id": int(line_list[0]),
                            "width": int(line_list[1]),
                            "height": int(line_list[2]),
                            "x": int(line_list[3]),
                            "y": int(line_list[4])}
            elif len(line_list) == 4:
                dict_obj = {"id": int(line_list[0]),
                            "size": int(line_list[1]),
                            "x": int(line_list[2]),
                            "y": int(line_list[3])}
            obj = cls.create(**dict_obj)
            res.append(obj)
        return res
