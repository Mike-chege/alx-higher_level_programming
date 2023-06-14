#!/usr/bin/python3
# Task 11
"""Class defintion based on 10-student.py"""


class Student:
    """Class Student definition"""

    def __init__(self, first_name, last_name, age):
        """
        instantiation of names and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieving dictionary representation of a student
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        """
        for ky, val in json.items():
            setattr(self, ky, val)
