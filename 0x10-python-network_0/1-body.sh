#!/bin/bash
#script that takes a URL, sends a request, and displays the size of the body
curl -s -L -X GET "$1"
