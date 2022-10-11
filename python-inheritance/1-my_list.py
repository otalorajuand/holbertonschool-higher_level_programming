#!/usr/bin/python3
"""
    this modules contains the class MyList
"""

class MyList(list):
    """This class inherits from list"""

    def print_sorted(self):
        """This methods prints the sorted self"""
        print(sorted(self))
