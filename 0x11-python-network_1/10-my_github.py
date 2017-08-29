#!/usr/bin/python3
# takes in github credentials ans displays the id
from requests import get
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    response = get(url, auth=HTTPBasicAuth(user, passwd)).json()
    print(response.get('id'))
