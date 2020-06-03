#!/usr/bin/python3
"""
student class
"""


class Student:
    """student Attributs"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation"""
        if attrs is None:
            return self.__dict__
        newdict = {}
        for att in attrs:
            try:
                new_dict[att] = self.__dict__[att]
            except:
                pass
        return newdict
