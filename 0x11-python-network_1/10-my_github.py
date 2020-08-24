#!/usr/bin/python3
"""  script that consume de Api from github and print user id """
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=auth)
    resp = r.json()
    print(resp.get("id"))
