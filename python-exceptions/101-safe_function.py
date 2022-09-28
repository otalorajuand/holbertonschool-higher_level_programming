#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely.

        Arguments:
        fct: The input function.
        args: The arguments of the function.
    """
    try:
        res = fct(*args)
    except (ZeroDivisionError, IndexError) as ex:
        print('Exception: {}'.format(ex), file=sys.stderr)
        return (None)
    return (res)
