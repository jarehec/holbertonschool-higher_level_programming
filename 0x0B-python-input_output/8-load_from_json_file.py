#!/usr/bin/python3
import json


def load_from_json_file(filename):
    'returns an object from a  json file'
    with open(filename, 'r') as obj:
        return json.loads(obj.read())
