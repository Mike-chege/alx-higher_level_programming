#!/usr/bin/python3

def safe_print_list(my_list=[] x=0):
    i = 0
    count = 0
    while i < x:
        try:
            if isinstance(my_list[i], (int, str)):
                print(my_list[i], end=' ')
                count += 1
            else:
                print("Error: Element is not an integer or string")
        except IndexError:
            break
        i += 1
    print('\n')
    return count
