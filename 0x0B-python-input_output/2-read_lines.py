#!/usr/bin/python3
""" Prints a file """


def read_lines(filename="", nb_lines=0):
    """ Pprint line """
    with open(filename, 'r', encoding='utf8') as file:
        if nb_lines <= 0:
            for ln in file:
                print(ln)
        else:
            for ln in range(nb_lines):
                print(file.readline(), end="")
