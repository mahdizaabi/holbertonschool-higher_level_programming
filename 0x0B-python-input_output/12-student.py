#!/usr/bin/python3
"""
student class
"""


class Student:
    """student attributs"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__

    def to_json(self, attrs=None):

        new_dic = {}
        if attrs:
            for att in attrs:
                if att in self.__dict__.keys():
                    new_dic[att] = self.__dict__[att]
            return new_dic
        else:
            return self.__dict__
