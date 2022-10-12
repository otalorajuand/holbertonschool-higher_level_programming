#!/usr/bin/python3
"""
This module contains the function load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """This function reads a json representation string
    from a file and returns the python object converted from this json

    Attributes:
        filename (str): The name of the file"""

    with open(filename, encoding="utf-8") as f:
        return (json.loads(f.read()))
