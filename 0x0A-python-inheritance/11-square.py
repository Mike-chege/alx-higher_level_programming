#!/usr/bin/python3
"""class definition"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square inheriting Rectangle
    """
    def __init__(self, size):
        """
        instantiation method for class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        overide str method for class
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
