#!/usr/bin/python3
# gets the X-Request-Is from the response
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as headers:
        headers = headers.info()
        print("{}".format(headers.get('X-Request-Id')))
