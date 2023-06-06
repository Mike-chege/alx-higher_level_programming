#!/usr/bin/python3
# Task 4 Text indentation
""" prints a text with 2 new lines after each given character"""


def text_indentation(text):
    """
    text_indentation function
    prints a string of text with 2 new lines after '.', '?', and ':'
    tests for the file are in directory tests/5-text_indentation.txt
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    specials = ['.', '?', ':']
    for ch in text:
        string += ch
        if ch in specials:
            string += "\n\n"
    print(string, end='')
