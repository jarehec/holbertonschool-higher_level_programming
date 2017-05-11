#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    keys = list(sorted(my_dict.keys()))
    val = list(my_dict.values())
    for i in range(len(keys)):
        print("{:s}: {}".format(keys[i], val[i]))
