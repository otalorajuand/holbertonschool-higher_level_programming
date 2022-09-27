#!/usr/bin/python3


def roman_to_int(roman_string):

    """converts a Roman numeral to an integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    number = 0
    symbols = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    last_entry = 1000

    for letter in roman_string:
        digit = symbols[letter]

        number += digit

        if last_entry < digit:
            number -= 2 * last_entry

        last_entry = digit

    return (number)
