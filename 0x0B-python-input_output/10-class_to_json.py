#!/usr/bin/python3
def class_to_json(obj):
    'returns a dictionary description with simple data structure'
    return obj.__dict__
