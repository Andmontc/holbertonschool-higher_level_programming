#!/bin/bash
# script that request an status
curl -s -o /dev/null -w '%{http-code}' "$1"
