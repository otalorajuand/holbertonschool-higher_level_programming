#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    """prints the elements of a matrix
        @matrix: The matrix to be printed.
        Return: Nothing"""

    if matrix == [[]]:
        return None

    for row in matrix:
        for col in range(len(row) - 1):
            print("{:d}".format(row[col]), end=" ")
        print("{:d}".format(row[col + 1]))
