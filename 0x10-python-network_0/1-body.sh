#!/bin/bash
# Takes in a URL, sends GET to URL and displays body of responce
curl -s "$1" | sed -n '/<body>/,/<\/body>/p'
