#!/usr/bin/python3
def class_to_json(obj):
    'returns a dictionary description with simple data structure'
    try:
        return obj.__dict__
    except:
        pass
