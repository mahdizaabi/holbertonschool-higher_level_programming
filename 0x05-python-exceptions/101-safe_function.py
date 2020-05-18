#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
