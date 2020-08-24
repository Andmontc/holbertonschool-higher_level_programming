#!/usr/bin/python3
"""  script that takes in a URL send request and show error code """
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(Error code: e.code)
