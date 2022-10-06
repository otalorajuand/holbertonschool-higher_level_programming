#!/usr/bin/python3
import numpy as np
"""This is the "101-lazy_matrix-mul" module.
The example module supplies one function, lazy_matrix_mul().  For example,
>>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
"""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Attributes:
    m_a: first matrix
    m_b: second matrix
    Returns: The resulting matrix."""

    if type(m_a) is not list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if type(m_b) is not list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_a == [] or m_a == [[]]:
        raise ValueError(r"m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError(r"m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
        if len(row) != len(m_a[0]):
            raise TypeError('setting an array element with a sequence.')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('invalid data type for einsum')

    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')
        if len(row) != len(m_b[0]):
            raise TypeError('setting an array element with a sequence.')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('invalid data type for einsum')

    if len(m_a[0]) != len(m_b):
        raise ValueError(f"shapes ({len(m_a)},{len(m_a[0])}) and ({len(m_b)},{len(m_b[0])}) \
not aligned: {len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)")

    a = np.array(m_a)
    b = np.array(m_b)

    return (a @ b)
