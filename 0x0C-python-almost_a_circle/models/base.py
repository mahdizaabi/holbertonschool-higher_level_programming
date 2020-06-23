#!/usr/bin/python3
"""Base module for all the classes"""
import json


class Base:
    """this class will be the Base of all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
