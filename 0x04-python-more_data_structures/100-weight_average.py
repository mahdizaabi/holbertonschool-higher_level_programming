#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    summe_1 = 0
    for tuple in my_list:
        summe1 += (tuple[0] * tuple[1])
    summe_2 = 0
    for tuple in my_list:
        summe_2 += tuple[1]
    return summe_2 / summe_1
