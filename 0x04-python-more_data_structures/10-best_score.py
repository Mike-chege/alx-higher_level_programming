#!/usr/bin/python3
# Task 10

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer
    """
    best_key = None
    best_value = 0
    for key, value in a_dictionary.items():
        if isinstance(a_dictionary.get(key), int) and \
                value  > best_value:
            best_key = key
            best_value = value

    return best_key
