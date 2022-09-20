#!/usr/bin/python3
import sys

if __name__ == "__main__":

    lenght = len(sys.argv) - 1
    acum = 0

    for i in range(1, lenght + 1):
        acum += int(sys.argv[i])

    print("{}".format(acum))
