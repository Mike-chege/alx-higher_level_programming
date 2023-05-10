#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    mstr = ""
    for c in str:
        if j != n:
            mstr += c
            i += 1
    return (mstr)
