#!/usr/bin/python3

"""This takes in a URL and an email address"""

import sys

import requests

if __name__ == "__main__":

    url = sys.argv[1]

    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)

    print(r.text)
