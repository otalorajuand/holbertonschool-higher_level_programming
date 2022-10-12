#!/usr/bin/python3
"""
This module contains the function save_to_json_string()
"""
import json

def save_to_json_file(my_obj, filename):
    """This function writes in a file the json representation of an object

    Attributes:
        my_obj (object): the object.
        filename: The name of the file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
