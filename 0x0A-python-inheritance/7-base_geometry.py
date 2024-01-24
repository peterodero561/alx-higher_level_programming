#!/usr/bin/python3
'''An empty BaseGeometry class'''


class BaseGeometry:
    '''Empty class'''

    def area(self):
        '''Raises a Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be an integer".format(name))
