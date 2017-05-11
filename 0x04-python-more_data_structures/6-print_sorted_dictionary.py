#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for keys, val in sorted(my_dict.items()):
        print("{:s}: {}".format(keys, val))
