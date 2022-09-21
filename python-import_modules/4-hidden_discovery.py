#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    lista = dir(hidden_4)

    for elem in lista:
        if elem[0] != "_":
            print("{}".format(elem))
