#!/usr/bin/python3
#displays the value of a specific header field of the response.
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.info()['X-Request-Id'])
