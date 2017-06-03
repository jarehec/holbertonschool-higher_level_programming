#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    'reads nb_lines of a text file'
    with open(filename, 'r', encoding='utf-8') as fname:
        if nb_lines <= 0 or nb_lines > len(list(fname)):
            print(fname.read(), end='')
        else:
            fname.seek(0)
            while nb_lines > 0:
                print(fname.readline(), end='')
                nb_lines -= 1
