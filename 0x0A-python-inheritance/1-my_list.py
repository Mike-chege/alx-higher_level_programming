#!/usr/bin/python3
# Task 1
"""A class that inherits from arg list"""


class MyList(list):
    """class my list definition"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
