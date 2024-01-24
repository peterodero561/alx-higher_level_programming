#!/usr/bin/python3
'''FUnction is_kind_of_class() that checks wheter
    obj is an instance a_class or class inheriting from a_class'''


def is_kind_of_class(obj, a_class):
    '''compares if obj is an instance of a_class or a class
    inheriting from a_class'''

    return isinstance(obj, a_class)
