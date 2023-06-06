#!/usr/bin/python3
"""Addition of two integers"""


def add_integer(a, b=98):
    """
    addition of two integers
    unit tests located directory tests/0-add_integer.txt
    which checks for type errors
    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
