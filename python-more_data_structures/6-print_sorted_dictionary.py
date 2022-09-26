#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    """prints a dictionary by ordered keys."""
    keys = sorted(list(a_dictionary))

    for elem in keys:
        print("{}: {}".format(elem, a_dictionary[elem]))
