#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is not None:
        big = 0
        for key, val in my_dict.items():
            big = val if val > big else big
        return big
