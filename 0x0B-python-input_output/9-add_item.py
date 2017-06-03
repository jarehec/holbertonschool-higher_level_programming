#!/usr/bin/python3
import json
import sys


load_from_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
filename = "add_item.json"
ac = len(sys.argv) - 1
try:
    list_t = load_from_file(filename)
except:
    list_t = []
with open(filename, 'a+') as fname:
    for i in range(1, ac + 1):
        list_t.append(sys.argv[i])
    save_to_json_file(list_t, filename)
