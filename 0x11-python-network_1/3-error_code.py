#!/usr/bin/python3
"""
    Display Error
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as req:
            print(req.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
