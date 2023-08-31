#!/bin/bash
# This script displays 200 status code body
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
