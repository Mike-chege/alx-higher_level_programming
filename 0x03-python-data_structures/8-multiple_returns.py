#!/usr/bin/python3
# Task 8

def multiple_returns(sentence):
    """
    returns tuple with the length of a string and its character
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
