#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a /= b
    except ZeroDivisionError:
        a = None
    finally:
        print("Inside result: ", end='')
    if a is not None:
        print("{:.1f}".format(a))
    else:
        print(None)
    return a
