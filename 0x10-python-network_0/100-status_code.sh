#!/bin/bash
# request given URL and displays status code of the response
curl -s -o /tmp/response.txt -w "%{http_code}" "$1" && cat /tmp/response.txt && rm /tmp/response.txt
