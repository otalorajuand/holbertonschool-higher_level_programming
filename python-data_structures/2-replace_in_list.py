#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    """replaces an element of a list at a specific position (like in C).
        @my_list: The list.
        @idx: The index of the element.
        @element: The new value of the element.
        Return: The new list.
    """

    if idx < 0 or idx >= len(my_list):
        return None

    my_list[idx] = element

    return my_list
