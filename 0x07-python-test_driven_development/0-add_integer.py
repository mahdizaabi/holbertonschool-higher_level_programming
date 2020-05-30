#!/usr/bin/Python3
'''
Integer/float addition Module
'''


def add_integer(a, b=98):
    '''
        check type and make operation
    '''
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
