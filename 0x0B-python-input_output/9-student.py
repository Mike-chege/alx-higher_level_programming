#!/usr/bin/python3
# Task 9
"""A class that defines a student"""


class Student:
    """Class student definition"""
    def __init__(self, first_name, last_name, age):
        """
        instantiation of names and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieving a dictionary representation of a student"""
        return self.__dict__
