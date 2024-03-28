#!/bin/bash
# Takes a URL and displays all http methods the server will accept
curl -s -X OPTIONS -i  "$1" | grep -i Allow | awk '{print $}'
