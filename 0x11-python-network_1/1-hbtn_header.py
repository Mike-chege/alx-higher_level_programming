#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
And displays the value of the X-Request-Id variable
Found in the header of the response
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
