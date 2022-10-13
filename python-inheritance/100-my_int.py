#!/usr/bin/python3
"""
This module contains the class My int
"""


class MyInt(int):
    """This class inherits from int and
    changes the methods eq and ne
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return not self.value == other

    def __ne__(self, other):
        return self.value == other
