#!/usr/bin/env python3
def no_c(my_string):
    listed_string = list(my_string)
    for s in range(len(my_string)):
        if listed_string[s] == 'c' or listed_string[s] == 'C':
            listed_string[s] = ""
    return(''.join(listed_string))
