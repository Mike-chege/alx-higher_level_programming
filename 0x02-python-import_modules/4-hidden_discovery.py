#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import py
    import sys

    py_compile.compile("hidden_4.py")

    import hidden_4

    names = dir(hidden_4)

    for name in sorted(names):
        if not name.startwith("__"):
            print(name)
