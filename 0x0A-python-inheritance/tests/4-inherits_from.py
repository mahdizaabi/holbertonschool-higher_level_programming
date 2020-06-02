#!/usr/bin/python3
"""
chack for sub class
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
