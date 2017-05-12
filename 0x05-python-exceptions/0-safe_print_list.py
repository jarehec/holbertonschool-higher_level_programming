#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for ele in range(x):
            i += 1
            print(my_list[ele], end='')
    except IndexError:
        print("")
        return ele
    print("")
    return i
