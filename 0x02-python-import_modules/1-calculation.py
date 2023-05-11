#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the results of add, sub, mul, and div"""
    from calculator_1 import add, sub, mul, div

    a = 1
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
