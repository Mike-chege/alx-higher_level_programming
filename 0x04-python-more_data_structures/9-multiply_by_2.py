#!/usr/bin/python3
# Task 9

def multiply_by_2(a_dictionary):
    """
    create a new dictionary with all values multiplied by 2
    """
    result = {}
    for key in a_dictionary:
        result[key] = a_dictionary[key] * 2

    return result
