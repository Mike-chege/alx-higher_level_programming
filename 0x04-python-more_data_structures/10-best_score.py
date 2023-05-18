#!/usr/bin/python3
# Task 10

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer
    """
    best_key = None
    best_value = 0
    if isinstance(a_dictionary, dict):
        for key, value in a_dictionary.items():
            if value > best_value:
                best_key = key
                best_value = value

    return best_key
