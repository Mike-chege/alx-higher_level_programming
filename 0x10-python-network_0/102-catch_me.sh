#!/bin/bash
# This script request to 0.0.0.0:5000/catch_me
curl -L -sX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
