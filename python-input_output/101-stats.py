#!/usr/bin/python3
"""
This module contains the function main()
"""
import sys
import signal


def main():
    """
    reads stdin line by line and computes metric
    """
    acum = 0
    num_lines = 1
    dict_lines = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

    for line in sys.stdin:

        striped_line = line.rstrip().split(" ")
        dict_lines[striped_line[7]] += 1

        
        if (num_lines % 10 == 0):
            print(f"File size: {acum}")
            for key in sorted(dict_lines):
                if dict_lines[key]:
                    print(f"{key}: {dict_lines[key]}")

        acum += int(striped_line[8])
        num_lines += 1


if __name__ == "__main__":
    main()
