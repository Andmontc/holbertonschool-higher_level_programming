#!/usr/bin/python3
"""python script that fetch a page"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: ' + str(type(html)))
        print('\t- content: ' + str(html))
        print('\t- utf8 content: ' + html.decode("utf-8"))
