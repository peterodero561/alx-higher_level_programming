#!/bin/bash
# Takes in a URL, sends GET to URL and displays body of responce
curl -s -o /dev/null -w "%{http_code}\n" $1 | grep -q 200 && curl -s $1
