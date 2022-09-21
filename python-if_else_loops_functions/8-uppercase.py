#!/usr/bin/python3


def uppercase(str):

    for letter in str:
        a = ord(letter)
        good = letter
        if (a >= 97 and a <= 122):
            good = chr(a - 32)
        print("{}".format(good), end="")
    print("{}".format(""))
