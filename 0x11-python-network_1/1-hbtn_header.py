#!/usr/bin/python3
"""  Script that takes in a URL, sends a request and displays the header"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
