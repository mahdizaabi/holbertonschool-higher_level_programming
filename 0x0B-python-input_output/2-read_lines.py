#!/usr/bin/python3
"""
"""


def read_lines(filename="", nb_lines=0):
    """
    """


    with open(filename, 'r', encoding='utf-8') as fx:
        if nb_lines <= 0:
            for ln in fx:
                print(ln)
        else:
            for ln in range(nb_lines):
                    print(fx.readline(), end='')
