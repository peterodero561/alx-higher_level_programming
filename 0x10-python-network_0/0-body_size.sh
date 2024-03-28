#!/bin/bash
# Script to send a request to a URL and display the size of the body of th responc
curl -sI "$1" | grep -i "content-length" | awk '{print $2}'
