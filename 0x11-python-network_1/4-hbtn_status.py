#!/usr/bin/python3
""" this script uses requests to fetche data from a url"""

import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    te = res.text
    print(f"Body response:\n\t- type: {type(te)}\n\t- content: {te}")
