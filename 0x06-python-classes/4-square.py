#!/usr/bin/python3


class Square:
    """
    class square attributes
    """
    def __init__(self, size=0):
        """
        initializating functions
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        (getter) for size attribute - method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        (setter) for size attribute method
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        calculating the area of the square
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        method validation checking for any errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
