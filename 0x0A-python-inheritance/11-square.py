#!/usr/bin/python3
# Task 11
"""A class definition"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class inheriting from Rectangle
    """
    def __init__(self, size):
        """
        initializing the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        using str method for overide
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
