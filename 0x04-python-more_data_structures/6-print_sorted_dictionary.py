#!/usr/bin/python3
# Task 6

def print_sorted_dictionary(a_dictionary):
    """
    print all dictionary by ordered keys
    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
