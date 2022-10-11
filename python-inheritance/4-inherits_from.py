#!/usr/bin/python3
"""
This module contains the function inherits_from()
"""

def inherits_from(obj, a_class):
    """Checks if obj is an subclass of a_class

    Attributes:
        obj (object): The object to be checked
        a_class (Class): The class the object is supossed to belong

    Return: True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; 
    otherwise False"""

    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
