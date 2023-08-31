#!/usr/bin/python3
"""
This script finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Function find_peak Definition
    Finds the pick of unsorted array
    """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    the_mid = int(length / 2)
    the_p = list_of_integers[the_mid]
    if the_p > list_of_integers[the_mid - 1] and the_p > list_of_integers[the_mid + 1]:
        return the_p
    elif the_p < list_of_integers[the_mid - 1]:
        return find_peak(list_of_integers[:the_mid])
    else:
        return find_peak(list_of_integers[the_mid + 1:])
