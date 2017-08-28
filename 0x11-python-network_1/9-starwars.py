#!/usr/bin/python3
# sends a POST request to the url with a name as a parameter
from requests import get
import sys

if __name__ == "__main__":
    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    response = get(url).json()
    print("Number of result: {}".format(response.get('count')))
    for item in response.get('results'):
        print(item.get('name'))
