#!/usr/bin/python3
'''
    Get header
'''


import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as req:
        print(dict(req.headers).get("X-Request-Id"))
