#!/usr/bin/python3
# Task 3
"""Square that defines a square by: (based on 2-square.py)"""


class Square:
    """
    class attributes:
    """
    def __init__(self, size=0):
        """
        initializing functions
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2
