#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    elif idx >= len(my_list):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
# don't use a.insert(idx, element)
# Insert methods modify ony le this, no return value !!!
