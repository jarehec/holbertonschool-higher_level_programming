#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    'writes an object to a text file in json repr'
    with open(filename, 'w') as jsndump:
        jsndump.write(json.dumps(my_obj))
