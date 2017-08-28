#!/usr/bin/python3
# sends a POST request to the passed URL
from requests import post
import sys

url = sys.argv[1]
email = {'email': sys.argv[2]}
response = post(url, email).content.decode('utf-8')
print(response)
