#!/usr/bin/python3
# Task 12
"""A class MyInt that inherits from int"""


class MyInt(int):
    """invert int operators == and != """
    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
