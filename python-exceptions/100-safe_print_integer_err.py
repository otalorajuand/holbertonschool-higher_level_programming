#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    """prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        print('Exception: {}'.format(ex), file=sys.stderr)
        return (False)
    return (True)
