#!/usr/bin/python3
# Task 4

def only_diff_elements(set_1, set_2):
    """
    find all elements present in only one set and add them to the set
    """
    only_diff = set()
    for elem in set_1:
        if elem not in set_2:
            only_diff.add(elem)
    for elem in set_2:
        if elem not in set_1:
            only_diff.add(elem)

    return only_diff
