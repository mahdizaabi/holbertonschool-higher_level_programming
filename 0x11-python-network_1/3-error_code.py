#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
import urllib.request
import sys
if __main__ == "__name__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
