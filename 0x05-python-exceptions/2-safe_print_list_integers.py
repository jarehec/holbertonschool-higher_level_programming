#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for ele in range(x):
        i += 1
        try:
            print("{:d}".format(my_list[ele]), end='')
        except (ValueError, TypeError):
            i -= 1
    print("")
    return i
