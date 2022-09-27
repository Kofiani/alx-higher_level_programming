#!/usr/bin/python3
''' create MyList to inherit from list '''


class MyList(list):
    ''' MyList is a subclass of list object '''

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
