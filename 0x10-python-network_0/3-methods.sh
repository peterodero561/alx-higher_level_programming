#!/bin/bash
# Takes a URL and displays all http methods the server will accept
curl -X OPTIONS -i -s "$1"
