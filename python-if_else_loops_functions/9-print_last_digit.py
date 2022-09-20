#!/usr/bin/python3

# print_last_digit - prints the last digit of a number.
# @number: The number to evaluate
# Return: The last digit of the number.


def print_last_digit(number):

    if number < 0:
        last_digit = (-1 * number) % 10
    else:
        last_digit = number % 10

    print(last_digit, end="")
    return(last_digit)
