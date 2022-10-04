#!/usr/bin/python3
"""This is the "0-add_integer" module.
The example module supplies one function, add_integer().  For example,

>>> add_integer(5, 10)
15"""

def add_integer(a, b=98):
    """Return the sum of a and b.
    a and b must be integers of floats.
    If float overflows, returns 98"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return (int(a) + int(b))
