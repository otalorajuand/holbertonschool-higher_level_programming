#!/usr/bin/python3


def uppercase(str):

    for letter in str:
        a = ord(letter)
        correct_letter = letter
        if (a >= 97 and a <= 122):
            correct_letter = chr(a - 32)
        print("{}".format(correct_letter), end="")
    print("{}".format(""))
