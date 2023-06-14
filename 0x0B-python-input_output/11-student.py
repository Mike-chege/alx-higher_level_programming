#!/usr/bin/python3
# Task 11
"""Class definition based on 10-student.py"""


class Student:
    """Class student definition"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
         """Retrieving a dictionary representation of student"""
         if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replacing all attributes of the student instance"""
        for k, v in json.items():
            setattr(self, k, v)
