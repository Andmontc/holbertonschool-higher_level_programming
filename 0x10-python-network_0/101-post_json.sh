#!/bin/bash
# script that sends a JSON POST request to a URL
curl -s -X POST -H "content-type: application/json" -d @"$2" "$1"
