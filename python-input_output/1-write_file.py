#!/usr/bin/python3
"""
This module contains the function write_file()
"""


def write_file(filename="", text=""):
    """This functions creates a file with the name of the content
    of the variable filename and writes the content
    of the variable text in it.

    Attributes:
        filename: The name of the new file
        text: The text content of the new file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        number_car = f.write(text)

    return (number_car)
