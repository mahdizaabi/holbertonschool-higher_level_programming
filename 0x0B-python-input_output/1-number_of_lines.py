#!/usr/bin/python3
"""
Nb lines 
"""


def number_of_lines(filename=""):
    """number of lines of a text file"""
    with open(filename, 'r', encoding='utf8') as fx:
        count = 0
        for line in fx:
            count += 1
        return count
