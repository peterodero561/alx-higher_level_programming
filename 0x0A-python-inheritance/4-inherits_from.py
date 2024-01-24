#!/usr/bin/python3
'''has function inherits_from() - checks if an object is an instance of
    a_class that inherited directly or indirectly'''


def inherits_from(obj, a_class):
    '''Checks whether a obj is an instance of a class that inherited'''
    return isinstance(obj, a_class) and not type(obj == a_class)
