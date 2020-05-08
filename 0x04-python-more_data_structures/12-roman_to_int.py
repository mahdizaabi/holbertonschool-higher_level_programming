#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) or not roman_string:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    for i in range(len(roman_string)):
        first = roman_string[i]
        if i < len(roman_string) - 1:
            second = roman_string[i + 1]
            if dict[second] <= dict[first]:
                number = number + dict[first]
            else:
                number = number - dict[first]
        else:
            number = number - dict[first]
    return number
