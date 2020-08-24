#!/usr/bin/python3
"""
Send a POST request with a letter a s a parameter
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) != 2:
        r = requests.post(url, data={'q': ''})
    else:
        r = requests.post(url, data={'q': sys.argv[1]})

    if r.json() and r.headers.get('content-type') == 'application/json':
        try:
            id = r.json().get('id')
            name = r.json().get('name')
            print("[{}] {}".format(id, name))
        except Exception as e:
            print("No result")
    elif r.headers.get('content-type') != "application/json":
        print("Not a valid JSON")
    else:
        print("No result")
