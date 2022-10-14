#!/usr/bin/python3
"""
This module contains the function append_after()
"""

def append_after(filename="", search_string="", new_string=""):
    """This function writes a file with the content of another file, and
    if in any line there is the certain string, a new string will be written
    down that line.

    Attributes:
        filename (str): The name of the new file
        search_string (str): The string to search.
        new_string (str): The string to be written if condition"""

    with open(filename, mode="r", encoding="utf-8") as f:
        Lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for line in Lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
