#!/usr/bin/python3
# Task 15

def complex_delete(a_dictionary, value):
    """
    delete all keys with the specified value
    """
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]

    return a_dictionary
