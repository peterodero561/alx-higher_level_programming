#!/usr/bin/python3
'''subclass MyList that inherits from superclass List'''


class MyList(list):
    '''class that creates a list
    Methods:
        print_sorted() - prints the list in ascending sort
    '''

    def print_sorted(self):
        '''prints a sorted list in ascending order'''
        sorted_list = sorted(self)
        print(sorted_list)
