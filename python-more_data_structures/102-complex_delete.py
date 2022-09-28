#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    """deletes keys with a specific value in a dictionary."""
    aux_dic = {k: v for k, v in a_dictionary.items()}

    for k, v in aux_dic.items():
        if v == value:
            del a_dictionary[k]

    return (a_dictionary)
