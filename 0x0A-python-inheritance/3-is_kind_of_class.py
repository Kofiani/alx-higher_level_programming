#!/usr/bin/python3
''' define a function to compare object instances '''


def is_kind_of_class(obj, a_class):
    ''' define a function to compare object instances '''

    if isinstance(obj, a_class):
        return True
    return False
