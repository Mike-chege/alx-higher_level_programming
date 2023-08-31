#!/bin/bash
# This script sends a request to a URL & displays only the status code of the response
curl -L -sX HEAD -w "%{http_code}" "$1"
