#!/usr/bin/python3
import json


def from_json_string(my_str):
    'returns an object repr by a json string'
    return json.loads(my_str)
