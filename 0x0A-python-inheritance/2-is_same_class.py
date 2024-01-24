#!/usr/bin/python3
'''FUnction is_same_class that checks wheter
    two objects are of the same class'''


def is_same_class(obj, a_class):
    '''compares if obj and a_class are of the same class'''

    return type(obj) == a_class
