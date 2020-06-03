#!/usr/bin/python3
"""
append text
"""


def append_write(filename="", text=""):
    """
    Append text
    """
    with open(filename, 'a', encoding='utf8') as file:
        n = file.write(text)
    return n
