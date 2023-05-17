#!/usr/binpython3
# Task 3

def common_elements(set_1, set_2):
    """
    find all common elements and add them to a set
    """
    common = set()
    for elem in set_1:
        if elem in set_2:
            common.add(elem)

    return common
