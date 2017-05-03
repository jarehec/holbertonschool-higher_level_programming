#!/usr/bin/python3
def remove_char_at(str, n):
    list(str)
    n_str = ''
    for c in range(len(str)):
        if c != n:
            n_str += str[c]
    return n_str
