#!/usr/bin/python3
def write_file(filename="", text=""):
    'writes a string to a text file'
    with open(filename, 'w') as fname:
        return fname.write(text)
