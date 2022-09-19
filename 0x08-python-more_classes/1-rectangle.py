#!/usr/bin/python3
''' Build on Rectangle class form task-0'''


class Rectangle:
    ''' Create a Rectangle '''

    def __init__(self, width=0, height=0):
        ''' construct instance variables width and height '''

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must >= 0')
        else:
            self.__height = value
