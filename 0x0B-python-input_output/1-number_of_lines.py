#!/usr/bin/pyhton3
"""
Nb of lines
"""


def number_of_lines(filename=""):
    """nb of lines"""

    g = 0
    with open(filename, 'r', encoding='utf-8') as filex:
        for i in filex:
            g += 1
        return g
