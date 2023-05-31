#!/usr/bin/python3


class Square:
    """
    class square attributes
    """
    def __init__(self, size=0):
        """
        initializating functions
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Ready to calculate the area of the square
        """
        return self.__size ** 2
