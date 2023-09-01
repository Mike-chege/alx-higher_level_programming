#!/usr/bin/python3
"""
This script takes 2 arguments and lists 10 commits
(from the most recent to oldest)
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    request = requests.get(url)
    commits = request.json()
    try:
        for item in range(10):
            print("{}: {}".format(
                commits[item].get("sha"),
                commits[item].get("commit").get("author").get("name")))
    except IndexError:
        pass
