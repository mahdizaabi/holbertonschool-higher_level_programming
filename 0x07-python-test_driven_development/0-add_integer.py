#!/usr/bin/Python3
'''
Integer/float addition Module
'''


def add_integer(a, b=98):
    '''
        check type and make operation
    '''

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
