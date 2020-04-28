#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            x = chr(ord(x) - (ord('a') - ord('A')))
        print("{:s}".format(x), end='')
    print("")
