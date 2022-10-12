#!/usr/bin/python3
"""
This module contains the function append_file()
"""


def append_write(filename="", text=""):
    """This functions appends to the file with the name of the content
    of the variable filename the content
    of the variable text.

    Attributes:
        filename: The name of the new file
        text: The text to append of the file"""

    with open(filename, mode="a", encoding="utf-8") as f:
        number_car = f.write(text)

    return (number_car)
