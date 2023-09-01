#!/usr/bin/python3
"""
This script takes in a letter and sends a POST
Request to http://0.0.0.0:5000/search_user
With the letter as a parameter
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        letter = ""
    else:
        sys.argv[1]

    query = {"q": letter}
    request = requests.post("http://0.0.0.0:5000/search_user", query)

    try:
        response = request.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

