#!/usr/bin/python3
# displays the body of the response or error code if URLError
from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as html:
            html = html.read()
            print("{}".format(html.decode('utf-8')))
    except error.URLError as err:
        print("Error code: {}".format(err.code))
