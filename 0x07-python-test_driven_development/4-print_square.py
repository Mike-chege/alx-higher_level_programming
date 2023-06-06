#!/usr/bin/python3
# Task 3
"""A function that prints a square with the character #"""


def print_square(size):
    """
    print_square function
    prints a square of any given size
    tests for the file are in the directory tests/4-print_square.txt
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    size = int(size)  # if it was a float convert it
    i = 0

    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print('#', end='')
        print()
