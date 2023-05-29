#!/usr/bin/python3
# Task 9

def magic_calculation(a, b):
    count = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                count += a**b / i
        except:
            count = b + a
            break
        return count
