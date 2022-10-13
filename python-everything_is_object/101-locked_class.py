#!/usr/bin/python3
"""
This module contains the class LockedClass
"""


class LockedClass:
    """This class only allows to assign attributes with
    the name first_name"""

    __slots__ = ['first_name']
