#!/usr/bin/python3
# sends a POST request to the url with a letter as a parameter
from requests import post
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) < 2:
    q = {'q': ''}
else:
    q = {'q': sys.argv[1]}
try:
    response = post(url, q).json()
except ValueError:
    print("Not a valid JSON")
if response == {}:
    print("No result")
else:
    print("[{}] {}".format(response['id'], response['name']))
