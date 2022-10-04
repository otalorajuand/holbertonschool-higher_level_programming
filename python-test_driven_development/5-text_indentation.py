#!/usr/bin/python3
"""This is the "5-text_indentation" module.
The example module supplies one function, text_indentation().  For example,
>>> text_indentation("Hello world. Who's there? Just me: Juan")
Hello world.

Who's there?

Just me:

Juan
"""


def text_indentation(text=""):
    """prints a text with 2 new lines after each of these characters:
    ., ? and :.
    The type of the text must be an string"""

    if type(text) is not str:
        raise TypeError('text must be a string')

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print()
            print()
            i += 1
        i += 1
