#!/usr/bin/python3
# gets the X-Request-Is from the response
from urllib import request
import sys

url = sys.argv[1]
headers = request.urlopen(url).info()
print("{}".format(headers.get('X-Request-Id')))
