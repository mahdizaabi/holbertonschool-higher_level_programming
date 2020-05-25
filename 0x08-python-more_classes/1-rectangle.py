#!/usr/bin/python3
'''class that defines new Rectangle '''


class Rectangle:
    '''new Class'''

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' a property to retrieve the value of width '''
        return(self.__width)

    @width.setter
    def width(self, value):
        ''' property setter to set the value of width '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):
        ''' propoerty setter to set the value of hight '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
