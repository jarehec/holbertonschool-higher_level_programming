#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status
from requests import get

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = get(url).content.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content {}"
          .format(type(response), response))
