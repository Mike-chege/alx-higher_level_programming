#!/usr/bin/python3

if __name__ == "__main__":
    """output is the result of all arguments"""
    import sys

    args = [int(arg) for arg in sys.argv[1:]]

    result = sum(args)

    print("{}".format(result))
