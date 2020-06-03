#!/usr/bin/python3
"""
"""


def read_lines(filename="", nb_lines=0):
    """
    """

    g = 0
    c = 1
    with open(filename, 'r', encoding='utf-8') as fx:
        for i in fx:
            g += 1
        fx.seek(0)
        if nb_lines <= 0 or nb_lines >= g:
            print(fx.read(), end='')
        else:
            for d in fx:
                if c <= nb_lines:
                    print(d, end='');
                    c += 1
