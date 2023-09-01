#!/usr/bin/python3
"""
This script takes in a URL and an email address,
Sends a POST request to the passed URL with the
Email as a parameter, and finally displays the
Body of the response
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    request = requests.post(url, mail)
    print(request.text)
