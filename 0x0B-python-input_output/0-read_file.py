#!/usr/bin/python3
# Task 0
"""Reading text file(UTF8) and print it to stdout"""


def read_file(filename=""):
    """"prints the tesxt file (UTF8) to stdout"""
    with open(filename, encoding="utf-8") as newfile:
        print(newfile.read(), end="")
