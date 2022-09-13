#!/usr/bin/python3
''' Introduce @property and setter to the class'''


class Square:
    ''' introduced the pythonic way to add getter and setter to a class '''
    def __init__(self, size=0):
        self.size = size

    @property
    ''' returns the value of size '''

    def size(self):
        return self.__size

    @size.setter
    '''sets the value of size to an integer >= 0 '''

    def size(self, value):
        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        ''' return the area of the square '''
        return self.__size ** 2
