#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    mstr = ""
    for c in str:
        if i != n:
            mstr += c
       i += 1
    return (mstr)
