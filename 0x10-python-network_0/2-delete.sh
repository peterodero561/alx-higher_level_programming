#!/bin/bash
# send DELETE request to URL passed a 1st arg and displayb body of respose
curl -x DELETE -s "$1"
