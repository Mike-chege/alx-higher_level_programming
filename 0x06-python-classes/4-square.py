#!/usr/bin/python3
# Task 4
"""Square that defines a square by: (based on 3-square.py)"""


class Square:
    """
    class attributes:
    """
    def __init__(self, size=0):
        """
        initializing functions
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        (getter) for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        (setter) for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
