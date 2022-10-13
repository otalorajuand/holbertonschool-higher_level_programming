#!/usr/bin/python3
"""
This module contains the class Students
"""


class Student:
    """This class defines a student
    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        original_attrs = self.__dict__

        if attrs is None:
            return (original_attrs)
        return ({key: value for key, value in original_attrs.items()
                if key in attrs})

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
