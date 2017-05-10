#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    for i in range(2):
        a.append(0)
        b.append(0)
    new_t = (a[0] + b[0], a[1] + b[1])
    return new_t
