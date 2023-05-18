#!/usr/bin/python3
# Task 8

def simple_delete(a_dictionary, key=""):
    """
    delete the key from the dictionary if it exists
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
