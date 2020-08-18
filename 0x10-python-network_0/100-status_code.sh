#!/bin/bash
# script that request an status
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
