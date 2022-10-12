#!/usr/bin/python3
"""
This module contains the function from_json_string()
"""
import json


def from_json_string(my_str):
    """Returns the python represention of the json string

    Attributes:
        my_str (str): The string containing the json to convert."""
    return (json.loads(my_str))
