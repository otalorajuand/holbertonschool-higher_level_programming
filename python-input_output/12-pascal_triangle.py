#!/usr/bin/python3
"""
This module contains the function pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n

    Attributes:
        n (int): The height of the triangle
    """
    if n <= 0:
        return ([])

    res = [[1]]

    for i in range(n - 1):

        aux_list = [1]

        for j in range(len(res[i]) - 1):
            aux_list.append(res[i][j] + res[i][j + 1])
        aux_list.append(1)
        res.append(aux_list)
    return (res)
