#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for a in range(x):
            print("{:d}".format(my_list[a]), end='')
        print()
        return(my_list[x-1])
    except IndexError:
        print()
        return(my_list.pop())
