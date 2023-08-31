#!/usr/bin/env bash
# This script takes in a URL, sends a request to that URL,
# And displays the size of the body of the response

url="$1"
response=$(curl -sI "$url" | grep -w "content-length" | cut -f2 -d' ')

echo $response
