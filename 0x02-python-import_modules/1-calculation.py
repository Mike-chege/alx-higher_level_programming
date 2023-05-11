#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    addition = add(a, b)
    difference = sub(a, b)
    product = mul(a,b)
    quotient = div(a, b)

    print("The sum of {} and {} is {}".format(a, b, addition))
    print("The difference between {} and {} is {}".format(a, b, difference))
    print("The product of {} and {} is {}".format(a, b, product))
    print("The quotient of {} and {} is {}".format(a, b, quotient))
