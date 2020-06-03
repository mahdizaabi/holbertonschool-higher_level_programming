#!/usr/bin/python3
"""
Contains the read_file function
"""


def read_file(filename=""):
    """
    Read a etxt file
    """

    with open(filename, "r", encoding='utf-8') as filex:
        print(filex.read(), end='')
