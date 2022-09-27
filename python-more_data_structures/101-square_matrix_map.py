#!/usr/bin/python3

def square_row(lista):
    return (list(map(lambda x: x ** 2, lista)))

def square_matrix_map(matrix=[]):

    """computes the square value of all integers of a matrix."""
    return (list(map(square_row, matrix)))
