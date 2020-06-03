#!/usr/bin/python3
"""

"""


def append_write(filename="", text=""):
    """

    """
    with open(filename, 'a', encoding='utf8') as file:
        return(file.write(text))
    
       
