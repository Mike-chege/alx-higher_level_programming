#!/usr/bin/python3
# Task 2

def uniq_add(my_list=[]):
    """
    compute the sum of all unique integers
    """
    unique_integers = set()

    for elem in my_list:
        if isinstance(elem, int):
            unique_integers.add(elem)

    result = sum(unique_integers)

    return result
