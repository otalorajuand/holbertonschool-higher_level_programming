#!/usr/bin/python3
"""
This module contains the function class_to_json
"""


def class_to_json(obj):
    """This functions returns a dictionary with an objects attibutes

    Attributes:
        obj (object): The object to inspect"""
    return (obj.__dict__)
