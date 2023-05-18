#!/usr/bin/python3
# Task 10

def best_score(a_dictionary):
    best_key = None
    best_value = float('-inf')
    for key in a_dictionary:
        if isinstance(a_dictionary[key], int) and a_dictionary[key] > best_value:
            best_key = key
            best_value = a_dictionary[key]

    return best_key

