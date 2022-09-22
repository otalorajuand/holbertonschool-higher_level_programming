#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num_1 = sys.argv[1]
    num_2 = sys.argv[3]
    operator = sys.argv[2]

    match operator:
        case '+':
            print('{} + {} = {}'.format(num_1, num_2, add(num_1, num_2)))
        case '-':
            print('{} - {} = {}'.format(num_1, num_2, sub(num_1, num_2)))
        case '*':
            print('{} * {} = {}'.format(num_1, num_2, mul(num_1, num_2)))
        case '/':
            print('{} / {} = {}'.format(num_1, num_2, div(num_1, num_2)))
        case other:
            print('Unknown operator. Available operators: +, -, * and /')

