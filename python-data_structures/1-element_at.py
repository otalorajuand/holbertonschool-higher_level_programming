#!/usr/bin/python3

def element_at(my_list, idx):

    """retrieves an element from a list like in C.
        @my_list: The list.
        @idx: The index of the element.
        Return: The element of array, or None if not
                exists.
    """

    if idx < 0 or idx > len(my_list):
        return None

    return my_list[idx]
