#!/usr/bin/python3
# gets the status code to the passed URL
from requests import get
import sys

response = get(sys.argv[1])
if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print("{}".format(response.content.decode('utf-8')))
