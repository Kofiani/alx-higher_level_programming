#!/usr/bin/python3
"""
    List recent commits on GitHub
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print(
                f"{commits[i].get('sha')}: "
                f"{commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
