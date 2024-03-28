#!/bin/bash
# Takes in a URL, sends GET to URL and displays body of responce
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1"
