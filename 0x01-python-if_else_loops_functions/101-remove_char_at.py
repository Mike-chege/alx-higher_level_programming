#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    mStr = ""
    for c in str:
        if i != n:
            mStr += c
        i += 1
    return (mStr)
