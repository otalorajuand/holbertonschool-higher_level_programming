#!/usr/bin/python3
import sys

if __name__ == "__main__":

    lenght = len(sys.argv) - 1

    if lenght > 1:
        print("{} arguments:".format(lenght))
    elif lenght == 1:
        print("{} argument:".format(lenght))
    else:
        print("{} arguments.".format(lenght))

    for i in range(1, lenght + 1):
        print("{}: {}".format(i, sys.argv[i]))
