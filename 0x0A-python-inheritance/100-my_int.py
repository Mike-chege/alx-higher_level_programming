#!/usr/bin/python3
# Task 12
"""A class MyInt that inherits from int"""


class MyInt(int):
    """invert int operators == and != """
    def __eq__(self, value):
        """overiding == operator with != """
    def __ne__(self, value):
        """overiding != operator with =="""
        return self.real == value
