#!/usr/bin/python3


def max_integer(my_list=[]):

    max = 0

    if my_list == [[]]:
        return None

    for elem in my_list:
        if elem > max:
            max = elem
    return max
