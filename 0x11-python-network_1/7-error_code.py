#!/usr/bin/python3
"""
This script takes in a URL,
Sends a request to the URL
And displays the body of the response
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
