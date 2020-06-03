#!/usr/bin/python3
"""
"""

def read_lines(filename="", nb_lines=0):
    """
    """

    g = 0
    c = 1
    with open(filename, 'r', encoding='utf-8') as file:
        for i in file:
            g += 1
        file.seek(0)
        if nb_lines <= 0 or nb_lines >= g:
            print(file.read(), end='')
        else:
            for d in file:
                if c <= nb_lines:
                    print(d, end='');
                    c += 1
