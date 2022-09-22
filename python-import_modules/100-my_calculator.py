#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num_1 = int(argv[1])
    num_2 = int(argv[3])
    operator = argv[2]

    if operator == "+":
        print('{} + {} = {}'.format(num_1, num_2, add(num_1, num_2)))
    elif operator == "-":
        print('{} - {} = {}'.format(num_1, num_2, sub(num_1, num_2)))
    elif operator == "*":
        print('{} * {} = {}'.format(num_1, num_2, mul(num_1, num_2)))
    elif operator == "/":
        print('{} / {} = {}'.format(num_1, num_2, div(num_1, num_2)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

