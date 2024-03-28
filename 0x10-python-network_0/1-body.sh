#!/bin/bash
# Takes in a URL, sends GET to URL and displays body of responce
curl -s "$1" | { read -r _; [ "${REPLY%% *}" = "200" ] && cat || echo "Error: Received HTTP status code ${REPLY%% *}"; }
