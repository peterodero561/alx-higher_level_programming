#!/bin/bash
# request given URL and displays status code of the response
response=$(curl -s -o /tmp/response.txt -w "%{http_code}" "$1") && echo "$response" | tail -n1 && rm /tmp/response.txt
