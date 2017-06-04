#!/usr/bin/python3
def class_to_json(obj):
    'returns a dictionary description with simple data structure'
    d = {'__dict__' : type(obj).__name__}
    d.update(vars(obj))
    return d
