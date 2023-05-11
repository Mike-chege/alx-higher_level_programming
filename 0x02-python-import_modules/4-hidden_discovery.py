#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4 as hidden

    names = dir(hidden_4)

    for name in dir(hidden):
        if not name.startwith("__"):
            print(name)
