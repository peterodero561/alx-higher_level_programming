#!/bin/bash
# Script to send a request to a URL and display the size of the body of th responce
curl -sI "$1" | wc -c
