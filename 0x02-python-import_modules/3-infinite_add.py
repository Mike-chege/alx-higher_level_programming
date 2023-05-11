#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    args = [int(arg) for arg in sys.argv[1:]]

    result = sum(args)

    print("{}".format(result))
