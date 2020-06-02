#!/usr/bin/python3
"""
check if the object is an instance of the class
or an instance from a class that inhirated from a base class
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
