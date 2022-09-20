#!/usr/bin/python3

# islower - checks for lowercase character.
# @c: the character to check.
# Return: Returns True if c is lowercase, False otherwise.

def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    return False
