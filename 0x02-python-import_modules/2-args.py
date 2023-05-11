#!/usr/bin/python3
if __name__ == "__main__":
    """outpus is the number of and list of arguments."""
    import sys
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("Number of argument(s): 0.")
    else:
        print("Number of arguments(s): {}.".format(num_args))

        if num_args == 1:
            print("Arguments.")
        else:
            print("Arguments: ")
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
