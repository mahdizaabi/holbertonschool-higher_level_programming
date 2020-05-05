#!/usr/bin/env python3
def no_c(my_string):
    copy = [l for l in my_string if l != 'c' and l != 'C']
    return ("".join(copy))
