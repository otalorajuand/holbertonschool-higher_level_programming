#!/usr/bin/python3
"""
This module contains the function read_file()
"""


def read_file(filename=""):
    """This function read text from a file and prints it in
    the standar ouput.

    Attributes:
        filename: The name of the file."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
