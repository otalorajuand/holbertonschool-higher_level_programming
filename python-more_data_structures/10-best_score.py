#!/usr/bin/python3


def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    maxim = 0

    if not a_dictionary:
        return (None)

    for key, value in a_dictionary.items():
        if value > maxim:
            best_key = key
            maxim = value
    return best_key
