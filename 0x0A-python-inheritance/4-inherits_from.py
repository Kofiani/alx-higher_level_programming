#!/usr/bin/python3
''' check if object is a class'''


def inherits_from(obj, a_class):
    ''' define a function to compare object instances '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
