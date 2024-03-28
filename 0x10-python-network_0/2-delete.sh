#!/bin/bash
# send DELETE request to URL passed a 1st arg and displayb body of respose
curl -X DELETE -s "$1"
