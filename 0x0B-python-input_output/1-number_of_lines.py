#!/usr/bin/pyhton3
"""
"""


def number_of_lines(filename=""):
    """
    """

    g = 0

    with open(filename, 'r', encoding="utf8") as filex:
        for i in filex:
            g += 1
        return g
