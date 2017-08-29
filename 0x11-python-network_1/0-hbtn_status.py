#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status
from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as html:
        html = html.read()
        print("Body response:")
        print("    - type {}".format(type(html)))
        print("    - content: {}".format(html))
        print("    - utf8 content: {}".format(html.decode('utf-8')))
