#!/usr/bin/python3


def weight_average(my_list=[]):

    """returns the weighted average of all integers tuple
    (<score>, <weight>)"""

    if not my_list:
        return (0)

    numerator = sum([elem[0] * elem[1] for elem in my_list]) 
    denominator = sum([elem[1] for elem in my_list])
    return (numerator / denominator)
