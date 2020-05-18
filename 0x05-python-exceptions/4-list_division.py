#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for j in range(list_length):
            d = my_list_1[j] / my_list_2[j]
    except ZeroDivisionError:
        print("division by 0")
        d = 0
    except (ValueError, TypeError):
        print("wrong type")
        d = 0
    except IndexError:
        print("out of range")
        d = 0
    finally:
        new_list.append(d)
    return(new_list)
