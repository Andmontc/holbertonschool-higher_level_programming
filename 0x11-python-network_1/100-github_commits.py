#!/usr/bin/python3
"""  script that consume de Api from github and print the 10 last commits"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
           sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commit = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commit[i].get('sha'),
                                  commit[i].get('commit').get('author')
                                  .get('name')))
    except:
        pass
