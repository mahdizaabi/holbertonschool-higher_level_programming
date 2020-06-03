#!/usr/bin/python3
"""
write to file
"""


def write_file(filename="", text=""):
    """
    write to file
    """
    with open(filename, 'w', encoding='utf8') as file:
        n = file.write(text)
    return(n)
