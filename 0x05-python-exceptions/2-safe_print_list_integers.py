#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    c = 0
    for i in range(x):
        try:
            my_list[i] += 0
            print(my_list[i], end='')
            c += 1
        except TypeError:
            ...
    print('')
    return(c)
