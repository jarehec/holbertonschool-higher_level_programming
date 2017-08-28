#!/usr/bin/python3
# sends a POST request to the passed URL
from urllib import parse, request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    email = parse.urlencode(email).encode('ascii')
    with request.urlopen(url, email) as response:
        print(response.read().decode('utf-8'))
