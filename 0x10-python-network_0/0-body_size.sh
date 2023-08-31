#!/bin/bash
# This script takes in a URL, sends a request to that URL,
# And displays the size of the body of the response

curl -sI "$1" | grep -w "Content-Length" | cut -f2 -d' '
