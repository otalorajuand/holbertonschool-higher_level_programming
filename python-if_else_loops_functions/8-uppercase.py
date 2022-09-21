#!/usr/bin/python3

# upptercase - prints a string in uppercase followed by a new line.
# @str: The input string.
# Return: Nothing.

def uppercase(str):

    for letter in str:
        a = ord(letter)
        if (a >= 97 and a <= 122):
            letter = chr(a - 32)
        print("{}".format(letter), end="")
    print("{}".format(""))
