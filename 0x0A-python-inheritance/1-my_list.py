#!/usr/bin/python3
class MyList(list):
    'Class that inherits from list'
    def print_sorted(self):
        'prints items in list sorted'
#        for i in self:
#            if isinstance(i, int) is False:
        print(sorted(self))
