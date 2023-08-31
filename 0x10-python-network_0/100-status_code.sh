#!/bin/bash
# This script sends a request to a URL & displays only the status code of the response
curl -sXL HEAD -w "%{http_code}" "$1"
