#!/usr/bin/python3
"""  script that takes in a letter and sends a POST request """
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})
    try:
        respjson = r.json()
        if respjson == {}:
            print('No result')
        else:
            print("[{}] {}".format(respjson.get("id"), respjson.get("name")))
    except ValueError:
        print("Not a valid JSON")
