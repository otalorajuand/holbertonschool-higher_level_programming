#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    """
        Prints all integers of a list, in reverse order.
        @my_list: The list.
        Return: Nothing.
    """

    if my_list:
        for i in range(1, len(my_list) + 1):
            print("{:d}".format(my_list[-i]))
