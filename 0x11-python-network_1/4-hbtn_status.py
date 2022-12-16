#!/usr/bin/python3
"""
    Request module
"""
import requests


if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f" - type: {type(req.text)}")
    print(f" - content: {req.text}")
