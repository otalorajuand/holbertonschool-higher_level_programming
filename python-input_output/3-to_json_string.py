#!/usr/bin/python3
"""
This module contains the function to_json_string()
"""
import json


def to_json_string(my_obj):
    """Returns the json represention of the object
    Attributes:
        my_obj (object): The object to convert."""
    return (json.dumps(my_obj))
